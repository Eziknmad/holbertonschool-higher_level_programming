# Python - Server-Side Rendering

A Flask-based project that explores server-side rendering (SSR) using Python, Flask, and the Jinja2 templating engine.

## Concepts Covered

- Server-side rendering vs client-side rendering
- Jinja2 templating: loops, conditionals, includes
- Reading and displaying data from JSON, CSV, and SQLite
- Flask routes and query parameters
- Reusable HTML components (header/footer)

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── template.txt
├── items.json
├── products.json
├── products.csv
├── products.db
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    └── product_display.html
```

## Tasks

### Task 0 - String Templating (`task_00_intro.py`)
A Python function `generate_invitations(template, attendees)` that reads a text template with placeholders (`{name}`, `{event_title}`, `{event_date}`, `{event_location}`) and generates personalized invitation files (`output_1.txt`, `output_2.txt`, etc.) for each attendee. Missing values are replaced with `N/A`. Includes input validation and error logging.

### Task 1 - Basic Flask Templates (`task_01_jinja.py`)
A Flask application with three routes (`/`, `/about`, `/contact`) that render HTML templates using Jinja2. Introduces reusable `header.html` and `footer.html` components included across all pages via `{% include %}`.

### Task 2 - Loops and Conditionals (`task_02_logic.py`)
Extends the Flask app with a `/items` route that reads a list from `items.json` and renders it dynamically using a `{% for %}` loop. Displays "No items found" when the list is empty using `{% if %}`.

### Task 3 - JSON and CSV Data Sources (`task_03_files.py`)
A `/products` route that accepts a `source` query parameter (`json` or `csv`) and an optional `id` to filter results. Reads product data from `products.json` or `products.csv` and renders it in a table via `product_display.html`. Returns appropriate error messages for invalid sources or missing products.

### Task 4 - SQLite Data Source (`task_04_db.py`)
Extends Task 3 by adding `source=sql` support. Reads product data from a SQLite database (`products.db`) using Python's `sqlite3` module. The same `product_display.html` template is used for all three data sources.

## Running the App

```bash
python3 task_04_db.py
```

Then visit:
- `http://localhost:5000/` — Home page
- `http://localhost:5000/about` — About page
- `http://localhost:5000/contact` — Contact page
- `http://localhost:5000/items` — Items list from JSON
- `http://localhost:5000/products?source=json` — Products from JSON
- `http://localhost:5000/products?source=csv` — Products from CSV
- `http://localhost:5000/products?source=sql` — Products from SQLite
- `http://localhost:5000/products?source=json&id=1` — Filter by product ID

## Requirements

- Python 3
- Flask (`pip install Flask`)
