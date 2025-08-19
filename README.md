# LaVida Soap Company Web Application

A Flask-based web application for LaVida Soap Company, showcasing their natural and handmade soap products.

## Project Structure

```
LaVida-Web-Application/
├── app.py              # Main Flask application file
├── static/            # Static files directory
│   ├── css/          # CSS stylesheets
│   │   ├── mobile.css
│   │   ├── new-styles.css
│   │   ├── notifications.css
│   │   ├── process-styles.css
│   │   └── styles.css
│   ├── images/       # Image assets
│   │   ├── 100-natural.png
│   │   ├── Charcoal-Detox-Soap.png
│   │   ├── Citrus-Fresh-Soap.png
│   │   └── ... (other images)
│   └── js/           # JavaScript files
│       └── main.js
└── templates/        # HTML templates
    ├── about.html
    ├── contact.html
    ├── index.html
    ├── process.html
    └── products.html
```

## Setup Instructions

1. Ensure you have Python installed on your system (Python 3.11 or later recommended)

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source .venv/bin/activate
     ```

4. Install required packages:
   ```bash
   pip install flask
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the website at: http://127.0.0.1:5000

## Features

- Responsive web design
- Product showcase
- Company information
- Manufacturing process details
- Contact information
- Static file serving for images, CSS, and JavaScript

## Routes

- `/` - Home page
- `/products` - Product catalog
- `/about` - About us page
- `/process` - Manufacturing process
- `/contact` - Contact information

## Development

The application is built using:
- Flask - Python web framework
- HTML5 & CSS3 for structure and styling
- JavaScript for interactivity
- Static file serving for assets

## File Descriptions

- `app.py` - Main Flask application file containing all route definitions
- `templates/*.html` - Jinja2 templates for each page
- `static/css/*.css` - Different CSS files for styling
- `static/js/main.js` - JavaScript for interactive features
- `static/images/*` - Image assets for the website

## Notes

- This is a development server. For production, use a proper WSGI server
- All static files are served through Flask's static file handling
- Templates use Jinja2 templating for dynamic content
- All routes are defined in app.py
