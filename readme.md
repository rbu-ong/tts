# Installation
Create virtual environment
```bash
python -m venv anyenvironmentfoldername
```

Activate virtual environment
```bash
anyenvironmentfoldername/Scripts/Activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
```bash
pip install -r requirements.txt
```
Database migration
```bash
python .\tts\manage.py migrate
```

Run project
```bash
python .\tts\manage.py runserver
```