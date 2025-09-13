import os
from resume_updater.gui import run_gui

if __name__ == "__main__":
    WORK_DIR = os.path.dirname(os.path.abspath(__file__))
    os.chdir(WORK_DIR)    
    run_gui()
