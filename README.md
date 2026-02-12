# SkillForge

SkillForge is a Django web application for organizing learning by managing skills, categories, resources, and learning paths in one place.

## Features

- Full CRUD for skills (`/skills/`)
- Full CRUD for learning paths (`/paths/`)
- Full CRUD for resources (`/resources/`)
- Full CRUD for categories (`/categories/`)
- Search on list pages
- Detail pages with related entities:
  - Skill -> related resources
  - Resource -> related skills
  - Category -> related skills
  - Learning path -> included skills
- Automatic slug generation for detail URLs
- Shared timestamps (`created_at`, `updated_at`) through an abstract base model

## Tech Stack

- Python
- Django 6
- PostgreSQL
- Django Templates (HTML)
- CSS (custom static files)

## Project Structure

```text
SkillForge/
├─ SkillForge/          # project settings and root URLs
├─ core/                # home/about, shared forms, validators, base model
├─ skills/              # skills domain (model, forms, views, urls)
├─ resources/           # resources domain (model, forms, views, urls)
├─ learning_paths/      # learning paths domain (model, forms, views, urls)
├─ category/            # categories domain (model, forms, views, urls)
├─ templates/           # global + app templates
├─ static/              # source static files
├─ staticfiles/         # collected static files
└─ manage.py
```

## Data Model Overview

- Category 1 -> N Skill
- Skill M <-> N Resource
- Skill M <-> N LearningPath

All major entities inherit `created_at` and `updated_at` from a shared abstract model in `core`.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd SkillForge
```

### 2. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If you already have `requirements.txt`:

```bash
pip install -r requirements.txt
```

If not, install the core packages manually:

```bash
pip install "Django>=6.0" psycopg[binary]
```

### 4. Configure PostgreSQL

Create a PostgreSQL database and update `SkillForge/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "skillforge",
        "USER": "postgres",
        "PASSWORD": "<your_password>",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin user (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Main Routes

- `/` -> Home
- `/about/` -> About
- `/skills/`
- `/paths/`
- `/resources/`
- `/categories/`

## Notes

- The current project stores DB credentials in `SkillForge/settings.py`. For production, move secrets to environment variables.
- `staticfiles/` contains collected static/admin assets and is usually generated.

## Suggested Next Improvements

1. Add `requirements.txt` or `pyproject.toml` for reproducible setup.
2. Add automated tests for core CRUD and validation flows.
3. Add `.env`-based configuration for secrets and DB settings.
4. Add Docker setup for app + PostgreSQL.
