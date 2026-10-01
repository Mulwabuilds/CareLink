# CareLink Deployment Guide

## 1. Purpose

This document describes how CareLink moves from local development to a production environment.

CareLink consists of:

```text
Frontend
   │
   ▼
Django REST API
   │
   ▼
PostgreSQL
```

The exact production hosting provider can be selected later.

---

# 2. Development Environment

The current development environment uses:

- Windows
- Python
- Django
- Django REST Framework
- PostgreSQL
- Git
- GitHub
- Visual Studio Code

The backend virtual environment is located at:

```text
backend/.venv/
```

The virtual environment must not be committed to Git.

---

# 3. Production Architecture

A production deployment can follow this structure:

```text
                 Internet
                    │
                  HTTPS
                    │
                    ▼
             Frontend / Client
                    │
                    ▼
              Django API
                    │
                    ▼
               PostgreSQL
```

A production environment should separate application configuration from source code.

---

# 4. Environment Variables

Production secrets should be provided through environment variables or a secure secret-management mechanism.

Typical variables include:

```text
SECRET_KEY
DEBUG
ALLOWED_HOSTS
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
CORS_ALLOWED_ORIGINS
CSRF_TRUSTED_ORIGINS
```

Real production credentials must never be committed to Git.

`.env.example` should document required variables without containing real secrets.

---

# 5. Production Settings

Before deployment:

- Set `DEBUG=False`.
- Configure production `ALLOWED_HOSTS`.
- Configure trusted CORS origins.
- Configure trusted CSRF origins.
- Use a strong secret key.
- Use secure database credentials.
- Enable HTTPS.
- Configure secure cookies and security headers.
- Configure production logging.

---

# 6. Install Dependencies

On the production server:

```bash
python -m pip install -r requirements.txt
```

A production environment should use an isolated Python environment.

---

# 7. Database Deployment

Create the production PostgreSQL database and configure the application to connect to it.

Then run:

```bash
python manage.py migrate
```

Migrations create and update the database schema according to the Django migration files.

---

# 8. Static Files

Before production deployment, collect Django static files:

```bash
python manage.py collectstatic
```

The production web server or hosting platform should serve the collected static assets appropriately.

---

# 9. Create an Administrator

A production administrator can be created with:

```bash
python manage.py createsuperuser
```

The administrator account should use a strong password.

---

# 10. Run Production Checks

Django provides deployment checks that should be run before release:

```bash
python manage.py check --deploy
```

Any important security warnings should be reviewed before deployment.

---

# 11. Application Server

Django's development server should not be used as the production application server.

A production deployment should use an appropriate WSGI or ASGI application server.

The selected hosting environment determines the exact command and configuration.

---

# 12. HTTPS

Production traffic should use HTTPS.

HTTPS protects information transmitted between:

```text
User
  │
  │ encrypted connection
  ▼
CareLink
```

This is particularly important because CareLink handles potentially sensitive information.

---

# 13. Database Backups

Production databases should have a backup strategy.

Backups should be:

- Automated where possible
- Stored separately from the primary database
- Tested through restoration procedures
- Protected from unauthorized access

A backup that has never been tested should not be assumed to be recoverable.

---

# 14. Logging and Monitoring

Production should monitor:

- Application errors
- Authentication failures
- Database errors
- API failures
- Server health
- Resource usage

Logs should not unnecessarily contain:

- Passwords
- JWT tokens
- Database credentials
- Sensitive patient information

---

# 15. Deployment Workflow

Recommended workflow:

```text
Local Development
       ↓
Run Tests
       ↓
Run Django Checks
       ↓
Commit Changes
       ↓
Push to GitHub
       ↓
Deploy Application
       ↓
Run Migrations
       ↓
Collect Static Files
       ↓
Run Deployment Checks
       ↓
Verify Application
```

---

# 16. Production Checklist

Before release:

- [ ] `DEBUG=False`
- [ ] Production `SECRET_KEY` configured
- [ ] Production database configured
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] HTTPS configured
- [ ] Allowed hosts configured
- [ ] CORS configured
- [ ] CSRF trusted origins configured
- [ ] Admin account secured
- [ ] Backups configured
- [ ] Logging configured
- [ ] Deployment checks completed
- [ ] Core authentication tested
- [ ] Patient/provider authorization tested

---

# 17. Deployment Strategy

The project can initially use a simple deployment architecture.

As CareLink grows, deployment can evolve toward:

```text
             Load Balancer
                   │
          ┌────────┴────────┐
          ▼                 ▼
     Django Instance    Django Instance
          │                 │
          └────────┬────────┘
                   ▼
              PostgreSQL
```

Caching, background workers, object storage, monitoring, and other infrastructure can be introduced when justified by project requirements.

---

# 18. Deployment Principle

The production environment should be treated as a separate environment from development.

Development configuration should never be copied blindly into production.
