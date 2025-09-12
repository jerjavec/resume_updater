from docx import Document
from docx2pdf import convert
from docx.shared import Pt
from datetime import datetime
from .logger_manager import log_update

def update_resume(docx_path, new_title, settings):
    """
    Updates the resume title in a Word document based on formatting or style detection,
    saves updated Word + PDF files, and logs the update.
    """
    doc = Document(docx_path)
    title_replaced = False

    for para in doc.paragraphs:
        if not para.text.strip():
            continue

        if para.alignment == 1:  # centered
            style_name = para.style.name.lower() if para.style else ""
            target_style = settings.get("resume_title_style", "").lower().strip()

            if target_style and style_name == target_style:
                para.text = new_title
                title_replaced = True
                break

            for run in para.runs:
                font_size = run.font.size
                bold = run.bold
                if bold and font_size == Pt(12):
                    para.text = new_title
                    title_replaced = True
                    break
                if bold and any(keyword in style_name for keyword in ["heading", "title"]):
                    para.text = new_title
                    title_replaced = True
                    break
        if title_replaced:
            break

    if not title_replaced:
        raise ValueError("Could not detect resume title to replace.")

    today = datetime.today().strftime("%Y%m%d")
    safe_title = new_title.replace(" ", "-")
    name = settings["name"]
    new_docx_filename = f"{today}-{name}_resume_{safe_title}.docx"
    pdf_filename = settings["pdf_filename"]

    doc.save(new_docx_filename)
    convert(new_docx_filename, pdf_filename)

    # Log this update
    log_update(docx_path, new_title, new_docx_filename, pdf_filename)

    return new_docx_filename, pdf_filename
