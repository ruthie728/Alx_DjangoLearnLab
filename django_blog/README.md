# Blog Post Management Features

## Features
- List all posts (public)
- View individual posts (public)
- Create new posts (authenticated users)
- Edit posts (author only)
- Delete posts (author only)

## Permissions
- Anyone can view posts.
- Only logged-in users can create posts.
- Only authors can edit or delete their own posts.

## Usage
- Visit /posts/ to see all posts.
- Click "Create New Post" to add a post.
- Use the "Edit" or "Delete" links on a post you authored to modify it.

Tagging & Search
----------------
- When creating or editing a post, add tags in the tags field separated by commas.
  Example: django, tutorial, backend

- Tags appear on post pages and link to pages showing all posts with that tag:
  /tags/<tag_name>/

- Use the search box (top of the page) to search by title, content, or tag.
  Search URL example: /search/?q=django

