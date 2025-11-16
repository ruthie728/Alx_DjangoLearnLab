# Permissions & Groups Setup

This project uses Django custom permissions for the Book model.

## Custom Permissions
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions

## Views Enforcement
Views use @permission_required decorators to restrict access.
