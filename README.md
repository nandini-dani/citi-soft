# CitiSoft — Client & Vendor Management Platform

A full-stack web platform for managing client and vendor relationships, built with a Python/Django backend and a responsive HTML/CSS frontend.

## 🚀 Features

- **Secure Login System** — Authentication with session management
- **Client Portal** — Dedicated interface for client-facing operations
- **Vendor Management** — Search, filter, and manage vendor records
- **Responsive UI** — Clean, accessible interface across devices
- **Search & Filter** — Fast lookup across client and vendor data

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Templating | Django Templates |
| Static Assets | CSS, custom styling |

## 📁 Project Structure

```
citi-soft/
├── citisoft/          # Core Django app
├── login/             # Authentication module
├── search_page/       # Search and filter functionality
├── static/            # CSS, JS, images
├── templates/         # HTML templates
└── manage.py          # Django management script
```

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/nandini-dani/citi-soft.git
cd citi-soft

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Then open `http://localhost:8000` in your browser.

## 💡 What I Learned

- Building full-stack applications with Django's MVC pattern
- Designing secure authentication flows
- Creating reusable HTML/CSS components
- Structuring a multi-module Django project

## 👩‍💻 Author

**Nandini Dani** — Senior Frontend Engineer  
[LinkedIn](https://www.linkedin.com/in/nandinidani/) • [GitHub](https://github.com/nandini-dani)