# SkillForge

SkillForge is a Django web application for organizing learning through Skills, Resources, Learning Paths, and Categories.

## Overview

- Framework: Django 6
- Database: PostgreSQL
- Template engine: Django Templates
- Styling: Bootstrap + custom CSS
- Authentication: intentionally not implemented (not required for this project)

## Core Features

- Full CRUD for:
  - Skills (`/skills/`)
  - Resources (`/resources/`)
  - Learning Paths (`/paths/`)
  - Categories (`/categories/`)
- Search on list pages
- Detail pages with related objects
- Slug-based detail URLs
- Shared timestamps via abstract base model (`created_at`, `updated_at`)
- Custom 404 page
- Custom template tag/filter usage (`custom_extras`)

## Data Model

- `Category` 1 -> N `Skill` (ForeignKey)
- `Skill` M <-> N `Resource` (ManyToMany)
- `Skill` M <-> N `LearningPath` (ManyToMany)

## Project Structure

```text
SkillForge/
|- SkillForge/          # settings, root urls, wsgi/asgi
|- core/                # home/about views, shared forms, validators
|- skills/              # skills domain
|- resources/           # resources domain
|- learning_paths/      # learning paths domain
|- category/            # categories domain + custom template tags
|- templates/           # global and app templates
|- static/              # source static assets
|- staticfiles/         # collected static assets
|- manage.py
`- requerments.txt
```

## Environment / Local Configuration

The project uses PostgreSQL with these settings in `SkillForge/settings.py`:

- `ENGINE`: `django.db.backends.postgresql`
- `NAME`: `skillforge`
- `USER`: `postgres`
- `PASSWORD`: set in local `settings.py`
- `HOST`: `127.0.0.1`
- `PORT`: `5432`

## Environment Variables

Set these variables locally before running the project:

- `DB_NAME=skillforge`
- `DB_USER=postgres`
- `DB_PASSWORD=your_password`
- `DB_HOST=127.0.0.1`
- `DB_PORT=5432`

Windows (PowerShell) example:

```powershell
$env:DB_NAME="skillforge"
$env:DB_USER="postgres"
$env:DB_PASSWORD="your_password"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="5432"
```

Before running the project, make sure your PostgreSQL server has:

1. A database named `skillforge`
2. A PostgreSQL user matching the configured credentials
3. Access rights for that user to the `skillforge` database

## Run Locally

### 1. Clone

```bash
git clone <your-public-repo-url>
cd SkillForge
```

### 2. Create virtual environment

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

```bash
pip install -r requerments.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run development server

```bash
python manage.py runserver
```

Open:

- App: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Main Routes

- `/` - Home
- `/about/` - About
- `/skills/` - Skills module
- `/resources/` - Resources module
- `/paths/` - Learning Paths module
- `/categories/` - Categories module

## Notes

- All pages are accessible from global navigation and footer links.
- Deletion operations use confirmation pages.
- The project includes built-in and custom template functionality.
