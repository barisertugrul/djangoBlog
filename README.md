# Django Blog Project

This Django project is a web application where you can create and manage blog posts.

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Setup

### 1. Clone the Project

```bash
git clone https://github.com/barisertugrul/djangoBlog.git
cd djangoBlog
```

### 2. Create and Activate a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install the following packages:

```bash
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install django-ckeditor
pip install Pillow
pip install django-cleanup
```

### 4. Create Necessary Folders

```bash
mkdir static
mkdir media
mkdir staticfiles
```

### 5. Database Operations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Project

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to view the project.

## Important Notes

- Before deploying to production, change `DEBUG = True` in `settings.py` to `False`.
- Keep the `SECRET_KEY` secure.
- Use a secure database in the production environment.

## Folder Structure

```
project_folder/
│
├── static/          # Static files (CSS, JS, images)
├── media/           # User uploads
├── staticfiles/     # Collected static files
├── templates/       # HTML templates
└── venv/            # Virtual environment
```
