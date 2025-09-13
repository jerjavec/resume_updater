import os, json

MAIN_DIR = os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main.py')))
SETTINGS_FILE = os.path.join(MAIN_DIR, "settings.json")

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        default_settings = {
            "name": "JohnDoe",
            "pdf_filename": "JohnDoe_Resume.pdf",
            "recent_files": [],
            "resume_title_style": ""
        }
        save_settings(default_settings)
        return default_settings
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)
