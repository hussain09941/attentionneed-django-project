# Attentionneed.com Django Website

A complete professional Django-based IT/technology company website.

## Features
- Home, About, Services, Projects, Blog, Blog Detail, Contact
- Signup, Login, Logout, User Dashboard
- Contact form saved in database
- Admin can manage services, projects, blogs, testimonials, team members, contact messages
- Responsive modern UI with dark blue, cyan, white and light gray theme

## Setup Commands

```bash
cd attentionneed_django_project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Add Sample Data
Login to admin and add:
- Services
- Projects
- Blog Posts
- Team Members
- Testimonials
