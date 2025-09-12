import os
from datetime import datetime

LOG_FILE = "resume_updater.log"

def log_update(original_file, new_title, new_docx, new_pdf):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | Resume: {original_file} | Title: {new_title} | Output: {new_docx}, {new_pdf}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def log_exists():
    return os.path.exists(LOG_FILE)

def view_log():
    """Open the log file in Notepad (Windows) or default editor (Mac/Linux)."""
    import subprocess, sys
    if not log_exists():
        return False
    try:
        if os.name == "nt":
            os.startfile(LOG_FILE)
        elif os.name == "posix":
            subprocess.call(("open" if sys.platform == "darwin" else "xdg-open", LOG_FILE))
        return True
    except Exception:
        return False
