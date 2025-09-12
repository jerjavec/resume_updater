import os
from resume_updater.logger_manager import log_update, log_exists, LOG_FILE, view_log

def test_log_update_creates_file(tmp_path):
    os.chdir(tmp_path)
    log_update("resume.docx", "Engineer", "out.docx", "out.pdf")
    assert os.path.exists(LOG_FILE)

def test_log_contains_entry(tmp_path):
    os.chdir(tmp_path)
    log_update("resume.docx", "Manager", "out.docx", "out.pdf")
    with open(LOG_FILE, "r") as f:
        content = f.read()
    assert "Manager" in content

def test_log_exists_function(tmp_path):
    os.chdir(tmp_path)
    assert not log_exists()
    log_update("resume.docx", "Dev", "out.docx", "out.pdf")
    assert log_exists()

def test_multiple_log_entries(tmp_path):
    os.chdir(tmp_path)
    log_update("resume.docx", "One", "out1.docx", "out1.pdf")
    log_update("resume.docx", "Two", "out2.docx", "out2.pdf")
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) == 2

def test_view_log_no_file(tmp_path):
    os.chdir(tmp_path)
    assert view_log() is False
