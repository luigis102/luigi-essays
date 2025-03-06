# Luigi's Blog

A minimalist personal blog built with Flask, featuring clean typography and content-first design.

## Features
- Clean, minimalist design
- Essay-focused layout
- Reading progress indicator
- Mobile-responsive design

## Project Structure
```
├── app.py
├── main.py
├── utils.py
├── content/
│   └── essays/
│       ├── future-of-learning.md
│       ├── reflection-on-progress.md
│       ├── sample-essay.md
│       └── simplicity-in-design.md
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── archive.html
    ├── base.html
    ├── essay.html
    └── index.html
```

## Setup
1. Clone this repository
2. Install dependencies:
```bash
pip install flask flask-flatpages email-validator
```
3. Run the application:
```bash
python main.py
```

## Content
Add new essays by creating `.md` files in the `content/essays/` directory with the following format:

```markdown
title: Your Essay Title
date: YYYY-MM-DD
description: Brief description of your essay
reading_time: estimated_minutes

Your essay content goes here...
```

## File Descriptions

- `app.py`: Main Flask application configuration and routes
- `main.py`: Application entry point
- `utils.py`: Utility functions for date formatting and reading time calculation
- `content/essays/`: Directory containing markdown files for blog posts
- `static/css/`: CSS styles
- `templates/`: HTML templates


## Deployment

The application is configured to run with Gunicorn for production deployment.