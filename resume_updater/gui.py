import tkinter as tk
from tkinter import filedialog, messagebox
import os

from .logic import update_resume
from .settings_manager import load_settings, save_settings
from .logger_manager import view_log

def run_gui():
    settings = load_settings()

    def choose_file():
        filepath = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if filepath:
            set_resume_path(filepath)

    def set_resume_path(filepath):
        entry_path.delete(0, tk.END)
        entry_path.insert(0, filepath)
        if filepath not in settings["recent_files"]:
            settings["recent_files"].insert(0, filepath)
        else:
            settings["recent_files"].remove(filepath)
            settings["recent_files"].insert(0, filepath)
        settings["recent_files"] = settings["recent_files"][:10]
        save_settings(settings)
        rebuild_recent_menus()
        set_status(f"Loaded: {os.path.basename(filepath)}")

    def run_update():
        docx_path = entry_path.get().strip()
        new_title = entry_title.get().strip()
        if not docx_path or not new_title:
            messagebox.showerror("Error", "Please select a file and enter a title.")
            set_status("Error: Missing file or title")
            return
        try:
            new_docx, new_pdf = update_resume(docx_path, new_title, settings)
            messagebox.showinfo("Success", f"Saved:\n{new_docx}\n{new_pdf}")
            set_status(f"Updated: {os.path.basename(new_docx)} + PDF")
            try:
                if os.name == "nt":
                    os.startfile(new_pdf)
            except Exception:
                pass
        except Exception as e:
            messagebox.showerror("Error", str(e))
            set_status(f"Error: {str(e)}")

    def open_settings_window():
        settings_window = tk.Toplevel(root)
        settings_window.title("Settings")
        settings_window.geometry("400x200")

        tk.Label(settings_window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_name = tk.Entry(settings_window, width=40)
        entry_name.insert(0, settings["name"])
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(settings_window, text="PDF Filename:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_pdf = tk.Entry(settings_window, width=40)
        entry_pdf.insert(0, settings["pdf_filename"])
        entry_pdf.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(settings_window, text="Title Style (optional):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_style = tk.Entry(settings_window, width=40)
        entry_style.insert(0, settings.get("resume_title_style", ""))
        entry_style.grid(row=2, column=1, padx=10, pady=5)

        def save_and_close():
            settings["name"] = entry_name.get().strip()
            settings["pdf_filename"] = entry_pdf.get().strip()
            settings["resume_title_style"] = entry_style.get().strip()
            save_settings(settings)
            messagebox.showinfo("Settings", "Settings saved successfully!")
            set_status("Settings updated")
            settings_window.destroy()

        tk.Button(settings_window, text="Save", command=save_and_close).grid(row=3, column=0, columnspan=2, pady=15)

    def rebuild_recent_menus():
        recent_menu.delete(0, tk.END)
        if not settings["recent_files"]:
            recent_menu.add_command(label="(No recent files)", state="disabled")
        else:
            for path in settings["recent_files"]:
                recent_menu.add_command(label=path, command=lambda p=path: set_resume_path(p))
        quick_menu.delete(0, tk.END)
        if not settings["recent_files"]:
            quick_menu.add_command(label="(No recent files)", state="disabled")
        else:
            for path in settings["recent_files"]:
                quick_menu.add_command(label=path, command=lambda p=path: set_resume_path(p))

    def set_status(message):
        status_var.set(message)
        root.update_idletasks()

    # --- GUI setup ---
    root = tk.Tk()
    root.title("Resume Updater")
    root.geometry("650x270")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open...", command=choose_file)

    recent_menu = tk.Menu(file_menu, tearoff=0)
    file_menu.add_cascade(label="Recent Files", menu=recent_menu)

    settings_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Settings", menu=settings_menu)
    settings_menu.add_command(label="Edit Settings", command=open_settings_window)
    settings_menu.add_command(label="View Log", command=view_log)

    tk.Label(root, text="Resume File (.docx):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_path = tk.Entry(root, width=55)
    entry_path.grid(row=0, column=1, padx=10, pady=5)

    button_frame = tk.Frame(root)
    button_frame.grid(row=0, column=2, padx=5, pady=5, sticky="w")
    tk.Button(button_frame, text="Browse", command=choose_file).pack(side="left")
    quick_button = tk.Menubutton(button_frame, text="Quick Access", relief="raised")
    quick_menu = tk.Menu(quick_button, tearoff=0)
    quick_button.config(menu=quick_menu)
    quick_button.pack(side="left", padx=5)

    tk.Label(root, text="New Job Title:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_title = tk.Entry(root, width=55)
    entry_title.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(root, text="Update Resume", command=run_update).grid(row=2, column=0, columnspan=3, pady=15)

    status_var = tk.StringVar()
    status_var.set("Ready")
    status_bar = tk.Label(root, textvariable=status_var, bd=1, relief="sunken", anchor="w")
    status_bar.grid(row=3, column=0, columnspan=3, sticky="we")

    rebuild_recent_menus()
    root.mainloop()
