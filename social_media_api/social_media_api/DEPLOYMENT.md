# Django REST API Deployment Documentation

## Project Information
- Repository: Alx_DjangoLearnLab
- Django Project Directory: social_media_api
- Framework: Django REST Framework

## Hosting Platform
- Platform: Render
- Reason for Choice: Easy deployment, GitHub integration, free tier support for Django applications

## Production Configuration

### Environment Variables
The following environment variables were configured on Render:
- SECRET_KEY
- DEBUG=False
- ALLOWED_HOSTS
- DATABASE_URL

### Django Production Settings
- DEBUG set to False
- ALLOWED_HOSTS configured for Render deployment
- Static files collected using `collectstatic`
- PostgreSQL database configured via DATABASE_URL

## Deployment Configuration Files

### Requirements
Dependencies are listed in:
- `requirements.txt`

### Procfile
The project uses Gunicorn as the WSGI server.
