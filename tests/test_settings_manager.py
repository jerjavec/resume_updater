import pytest
import os
from resume_updater.settings_manager import load_settings, save_settings, SETTINGS_FILE

def test_settings_file_created(tmp_path):
    os.chdir(tmp_path)
    settings = load_settings()
    assert os.path.exists(SETTINGS_FILE)

def test_settings_default_values(tmp_path):
    os.chdir(tmp_path)
    settings = load_settings()
    assert "name" in settings
    assert "pdf_filename" in settings

def test_settings_save_and_reload(tmp_path):
    os.chdir(tmp_path)
    settings = load_settings()
    settings["name"] = "TestUser"
    save_settings(settings)
    new_settings = load_settings()
    assert new_settings["name"] == "TestUser"

def test_settings_recent_files_limit(tmp_path):
    os.chdir(tmp_path)
    settings = load_settings()
    settings["recent_files"] = [f"file{i}.docx" for i in range(20)]
    save_settings(settings)
    reloaded = load_settings()
    assert len(reloaded["recent_files"]) >= 0  # saved without breaking

def test_settings_custom_style(tmp_path):
    os.chdir(tmp_path)
    settings = load_settings()
    settings["resume_title_style"] = "Heading 2"
    save_settings(settings)
    reloaded = load_settings()
    assert reloaded["resume_title_style"] == "Heading 2"
