# SkillForge

SkillForge is a Django web application for organizing personal learning. Each user can create categories, track skills, attach learning resources, group skills into learning paths, and manage everything from a profile dashboard.

## Overview

- Authentication with custom user model
- Personal profile with image upload
- Full CRUD for categories, skills, resources, and learning paths
- Per-user ownership for all main content
- Slug-based detail pages
- Authenticated REST API for skills
- PostgreSQL-based persistence
- Production-ready static file handling with WhiteNoise
- Gunicorn support for deployment
- Custom 404 and 500 pages

## Tech stack

- Python
- Django 6
- Django REST Framework
- PostgreSQL
- Gunicorn
- WhiteNoise
- Pillow
- python-dotenv
- Unidecode
- Django Templates
- Custom CSS

## Apps

- `accounts` - registration, login, profile view/update/delete, custom user model
- `skills` - skill CRUD and authenticated API endpoint
- `resources` - resource CRUD with links to skills
- `learning_paths` - learning path CRUD with grouped skills
- `category` - category CRUD
- `core` - home page, about page, shared base model, validators, error handlers

## Main routes

- `/` - home page
- `/about/` - about page
- `/registration/` - sign up
- `/login/` - login
- `/logout/` - logout
- `/profile/` - user profile
- `/categories/` - category management
- `/skills/` - skill management
- `/resources/` - resource management
- `/paths/` - learning path management
- `/api/skills/` - authenticated skills API
- `/admin/` - Django admin

## Data model summary

- `SkillForgeUser` extends `AbstractUser` and adds a profile image
- `Category` belongs to a user
- `Skill` belongs to both a category and a user
- `Resource` belongs to a user and can be attached to multiple skills
- `LearningPath` belongs to a user and can include multiple skills
- Main content models share `created_at` and `updated_at` timestamps through an abstract base model

## Project structure

```text
SkillForge/
|- SkillForge/        # settings, urls, wsgi, asgi
|- accounts/          # auth and user profile
|- category/          # categories
|- core/              # shared logic and static pages
|- learning_paths/    # learning paths
|- resources/         # learning resources
|- skills/            # skills and API
|- templates/         # HTML templates
|- static/            # source static files
|- staticfiles/       # collected static files for deployment
|- media/             # uploaded media
|- manage.py
|- requirements.txt
`- .env
```

## Environment variables

Create a `.env` file in the project root with values for:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

DB_NAME=skillforge
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@example.com
```

## Local development

### 1. Clone the repository

```bash
git clone https://github.com/jonkataBG47/SkillForge.git
cd SkillForge
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the PostgreSQL database

Create a PostgreSQL database and update the `.env` values to match it.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Deployment notes

- The project is configured to run with `gunicorn`
- Static files are collected into `staticfiles/`
- WhiteNoise is enabled for serving static assets
- Production hosts and trusted origins are controlled through `.env`
- Uploaded media is stored in `media/`

Example production commands:

```bash
python manage.py collectstatic --noinput
gunicorn SkillForge.wsgi:application
```

## API

Authenticated users can use:

- `GET /api/skills/` - list their own skills
- `POST /api/skills/` - create a new skill under their account

## Email behavior

After registration, the project sends a welcome email using Django's email backend configuration from `.env`.

## Testing

```bash
python manage.py test
```

## Notes

- Slugs are generated with `Unidecode` for cleaner URLs
- Uploaded profile images are stored under `media/profile_images/`
- In production, keep `DEBUG=False` and set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` correctly
