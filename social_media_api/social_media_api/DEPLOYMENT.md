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

# Deployment Documentation

## Deployment Steps
1. Code pushed to GitHub repository
2. Repository connected to Render
3. Root directory set to `social_media_api`
4. Environment variables configured on Render
5. Run `python manage.py collectstatic` locally
6. Application deployed successfully

## Live Application URL
https://social_media_api.onrender.com

## Monitoring and Maintenance
- Application logs monitored via Render dashboard
- Dependencies updated regularly
- Redeployment done after code changes
