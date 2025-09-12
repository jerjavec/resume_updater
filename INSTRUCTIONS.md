# Instructions

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install python-docx docx2pdf pytest
   ```
3. Run the app:
   ```bash
   python main.py
   ```

## GitHub Actions CI
1. Push the repository to GitHub.
2. The workflow is already configured at `.github/workflows/python-tests.yml`.
3. On every push or pull request to `main`, tests will automatically run.

## Running Tests
```bash
pytest tests
```
