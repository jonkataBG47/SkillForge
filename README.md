# SkillForge

SkillForge is a Django web application for planning and organizing learning content. Users can create categories, add skills, attach learning resources, combine skills into learning paths, and manage everything from a personal profile.

## What the project includes

- User registration, login, logout, profile update, and profile deletion
- Full CRUD for categories, skills, resources, and learning paths
- Per-user content ownership
- Search and detail pages with slug-based URLs
- Profile image upload support
- Auth-protected REST API endpoint for skills
- Celery task for registration email sending
- Shared timestamp base model for all main content types
- Custom 404 page and reusable template partials

## Tech stack

- Python
- Django 6
- Django REST Framework
- PostgreSQL
- Celery
- Redis
- Pillow
- Django Templates
- Custom CSS

## Main modules

- `accounts` - custom user model, authentication, profile management
- `category` - category CRUD
- `skills` - skill CRUD and API endpoint
- `resources` - resource CRUD and skill relationships
- `learning_paths` - learning path CRUD and skill grouping
- `core` - home, about, validators, base model, shared utilities

## Data model summary

- `SkillForgeUser` extends Django `AbstractUser` and supports profile images
- `Category` belongs to a user
- `Skill` belongs to a category and a user
- `Resource` belongs to a user and can be linked to multiple skills
- `LearningPath` belongs to a user and can include multiple skills
- All main content models inherit shared `created_at` and `updated_at` fields

## Main routes

- `/` - home page
- `/about/` - about page
- `/registration/` - user registration
- `/login/` - login
- `/logout/` - logout
- `/profile/` - user profile
- `/skills/` - skill management
- `/resources/` - resource management
- `/paths/` - learning path management
- `/categories/` - category management
- `/api/skills/` - authenticated skills API
- `/admin/` - Django admin

## Project structure

```text
SkillForge/
|- SkillForge/        # project settings, root urls, celery, asgi/wsgi
|- accounts/          # authentication and profile management
|- category/          # category app
|- core/              # shared logic, validators, base model, pages
|- learning_paths/    # learning path app
|- resources/         # resource app
|- skills/            # skill app and API
|- templates/         # global and app templates
|- static/            # source static files
|- media/             # uploaded profile images
|- manage.py
`- requirements.txt
```
## Local setup

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

Create a database named `skillforge` and make sure the configured PostgreSQL user has access to it.

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

## Optional services

If you want Celery tasks such as registration email sending to run asynchronously, start Redis and a Celery worker:

```bash
celery -A SkillForge worker --loglevel=info
```

If you do not want to run a worker during local development, set `CELERY_TASK_ALWAYS_EAGER=True`.

## API

The project currently exposes one API endpoint:

- `GET /api/skills/` - list the authenticated user's skills
- `POST /api/skills/` - create a skill for the authenticated user

Authentication is required for both operations.

## Testing

Run the test suite with:

```bash
python manage.py test
```

## Notes

- Slugs are generated automatically with `unidecode`, which helps transliterate non-Latin titles.
- Uploaded profile images are stored in `media/profile_images/`.
- Static files are served from `static/`, and collected output goes to `staticfiles/`.
