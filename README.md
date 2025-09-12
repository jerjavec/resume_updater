# Resume Updater

A desktop tool for updating job titles in Word resume files and generating PDFs. Built with Python, Tkinter, and python-docx.

## Features
- GUI with file selection and quick access
- Smart job title detection (formatting or style-based)
- Configurable settings stored in `settings.json`
- Recent files tracking (last 10 resumes)
- Logging to `resume_updater.log`
- GitHub Actions CI for tests

## Screenshots

### Main GUI
![Main GUI Screenshot](docs/images/gui.png)

### Settings Window
![Settings Screenshot](docs/images/settings.png)

### Log File Example
```
2025-09-10 15:42:31 | Resume: resume.docx | Title: IT Manager | Output: 20250910-JohnErjavec_resume_IT-Manager.docx, JohnErjavec_Resume.pdf
```

## Usage
1. Install dependencies:
```bash
pip install python-docx docx2pdf pytest
```
2. Run the app:
```bash
python main.py
```

## Running Tests
```bash
pytest tests
```

## GitHub Actions CI
The project includes a GitHub Actions workflow at `.github/workflows/python-tests.yml` that runs tests on pushes and pull requests.

## Roadmap
- Add profile management for different resume versions
- Enhance UI with icons and themes
- Improve detection for multiple resume styles

