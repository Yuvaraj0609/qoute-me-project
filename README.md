# Quote Me Project

This project is a Django-based web application that replicates the **"Quote Me"** section of [ParcelHero's landing page](https://www.parcelhero.com/). It allows users to get parcel delivery quotes by entering basic shipment details like origin, destination, parcel type, and dimensions.

## 🚀 Features

- Clean and responsive front-end with **Jinja templates**
- Dynamic form to get delivery quotes
- Integration with **MariaDB** for backend data handling
- User-friendly UX inspired by ParcelHero
- Modular Django app structure

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Jinja2
- **Database**: MariaDB
- **Templating Engine**: Jinja2 (Django's default)

## 📸 Screenshots

> <img width="959" alt="image" src="https://github.com/user-attachments/assets/06211903-a0f2-4d53-9c23-eab225447c33" />


## 📂 Project Structure

```bash
qoute-me-project/
├── manage.py
├── quote_me/              # Main Django app
│   ├── migrations/
│   ├── templates/
│   │   └── quote_me/
│   │       └── index.html
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── qoute_me_project/      # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md
