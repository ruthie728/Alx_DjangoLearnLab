# HTTPS and Secure Redirects

## HTTPS Configuration
- SECURE_SSL_REDIRECT = True → Forces HTTPS
- SECURE_HSTS_SECONDS = 31536000 → Enforces HSTS for 1 year
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True → HSTS applies to all subdomains
- SECURE_HSTS_PRELOAD = True → Allows browser preload lists

## Secure Cookies
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True

## Security Headers
- X_FRAME_OPTIONS = 'DENY'
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

## Deployment
- Ensure SSL/TLS certificates are installed.
- Redirect HTTP traffic to HTTPS in web server configuration.

## Security Review
These settings protect against:
- Man-in-the-middle attacks (HTTPS)
- Clickjacking (X_FRAME_OPTIONS)
- XSS (browser XSS filter and CSP)
- Cookie hijacking (secure cookies)