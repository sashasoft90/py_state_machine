call venv\Scripts\activate.bat
coverage run -m tests.runner
coverage html
pause
IF "%1"=="" cov_html.bat