# Centro de Bienestar

This repository hosts a **Next.js** web application packaged as a Progressive Web App (PWA) together with a **Django** backend. Both parts can run locally for development or be deployed through the provided Docker configuration.

## Project overview

- **backend/** – Django project with the API and administration site.
- **webapp/** – Next.js application used as the main frontend.
- **mobile/** – Capacitor configuration for building native Android/iOS wrappers.

The goal of the project is to offer a wellness platform where users interact through the PWA and services are managed by the Django backend.

## Environment setup

1. **Python 3.9+** is required for the backend.
2. **Node.js 18+** is recommended for the frontend.
3. Clone the repository and install the dependencies below.

### Backend

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy `.env` and adjust the variables such as `SECRET_KEY` and database credentials.

### Frontend

```bash
cd webapp
npm install
```

## Running the applications

### Django backend

```bash
cd backend
python manage.py migrate   # initial setup
python manage.py runserver
```

The server will be available on [http://localhost:8000](http://localhost:8000).

### Next.js app

```bash
cd webapp
npm run dev
```

This starts the frontend on [http://localhost:3000](http://localhost:3000).

## Building the PWA

1. Build the Next.js project:

```bash
cd webapp
npm run build
```

2. From the repository root, package the PWA assets into the `www` directory:

```bash
npm run build
```

The generated `www/` folder can then be used with Capacitor or served statically.

## Docker usage

To run the services in containers:

```bash
docker-compose up --build
```

The compose file starts individual containers for the users and products services and an Nginx gateway.

