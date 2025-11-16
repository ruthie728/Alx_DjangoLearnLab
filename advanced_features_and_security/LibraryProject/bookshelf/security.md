# Security Overview

This project implements best practices to secure the Django application.

## Key Security Features

- **DEBUG = False** in production
- **CSRF Protection:** All forms use `{% csrf_token %}`.
- **XSS & Browser Protections:**
  - SECURE_BROWSER_XSS_FILTER = True
  - SECURE_CONTENT_TYPE_NOSNIFF = True
- **Clickjacking Protection:**
  - X_FRAME_OPTIONS = 'DENY'
- **HTTPS-only Cookies:**
  - CSRF_COOKIE_SECURE = True
  - SESSION_COOKIE_SECURE = True
- **Content Security Policy (CSP):**
  - CSP_DEFAULT_SRC = 'self'
  - CSP_SCRIPT_SRC = 'self'
  - CSP_STYLE_SRC = 'self'
  - CSP_IMG_SRC = 'self'
  - CSP_FONT_SRC = 'self'