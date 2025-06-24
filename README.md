  # Inventory System

[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.1.1-green)](https://www.djangoproject.com/)

## Overview

Inventory System is a Django-based web application designed to manage product inventories efficiently. It provides RESTful APIs using Django REST Framework and includes management commands to populate and delete products. The project supports containerized deployment with Docker.

## Features

- Product inventory management
- REST API endpoints for CRUD operations
- Custom Django management commands for bulk operations
- Docker support for easy deployment
- Simple and clean UI with static assets and templates

## Installation

### Prerequisites

- Python 3.9+
- pip
- Docker (optional, for containerized deployment)

### Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd inventory_system
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. (Optional) Collect static files:

   ```bash
   python manage.py collectstatic
   ```

## Running the Project

### Locally

Start the development server:

```bash
python manage.py runserver
```

Access the app at [http://localhost:8000](http://localhost:8000).

### Using Docker

Build the Docker image:

```bash
docker build -t inventory-system .
```

Run the Docker container:

```bash
docker run -p 8000:8000 inventory-system
```

## Management Commands

The project includes custom management commands located in `inventory/management/commands`:

- `populate`: Populate the database with sample products.
- `delete_products`: Delete specific products.
- `delete_all_products`: Delete all products from the database.

Run a command like this:

```bash
python manage.py populate
```

## Running Tests

Run the test suite with:

```bash
python manage.py test
```

## Project Structure

```
inventory_system/
├── inventory/                # Main app with models, views, serializers, etc.
├── inventory_system/         # Project settings and URLs
├── static/                   # Static files
├── templates/                # HTML templates
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker container setup
└── db.sqlite3                # SQLite database file
```

## Contact

For questions or feedback, please open an issue or contact here.
