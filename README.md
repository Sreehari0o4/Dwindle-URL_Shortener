```markdown
# Dwindle – URL Shortener & Analytics

A full-stack **URL shortening service with real-time analytics**, built using **FastAPI, PostgreSQL, Redis, and Docker**.

Dwindle allows users to create short links, track how many people click them, and view analytics through a simple dashboard.

---

# Features

## URL Shortening
Generate short links for long URLs.

```

[https://example.com/some/very/long/url](https://example.com/some/very/long/url)
↓
[http://localhost:8000/abc123](http://localhost:8000/abc123)

```

## Custom Short Codes
Create your own readable links.

```

/github
/docs
/project

```

## Link Expiration
Links can expire after a specified time.

## Click Analytics
Track how many times each shortened link is used.

## Analytics Dashboard
View analytics through an interactive dashboard with charts.

## Redis Caching
Redirect performance is improved using Redis caching.

## PostgreSQL Database
Persistent storage for links and analytics.

## Docker Deployment
Run the entire stack using Docker containers.

---

# Architecture

```

Browser
↓
FastAPI API
↓
Redis Cache
↓
PostgreSQL Database

```

Redis caches frequently accessed short links to reduce database load.

---

# Tech Stack

### Backend
FastAPI  
SQLAlchemy ORM  
Alembic (Database migrations)

### Database
PostgreSQL

### Caching
Redis

### Frontend
HTML  
JavaScript  
Chart.js

### Infrastructure
Docker  
Docker Compose

---

# Project Structure

```

url-shortener/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── cache.py
│   ├── schemas.py
│
├── frontend/
│   ├── index.html
│   ├── analytics.html
│
├── alembic/
│   ├── versions/
│   ├── env.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
├── README.md
└── .gitignore

```

---

# Setup and Installation

You can run the project **either locally or using Docker**.

---

# Option 1 – Run Using Docker (Recommended)

This starts:

- FastAPI
- PostgreSQL
- Redis

### 1. Install Docker

https://www.docker.com/

---

### 2. Clone the Repository

```

git clone [https://github.com/YOUR_USERNAME/dwindle-url-shortener.git](https://github.com/YOUR_USERNAME/dwindle-url-shortener.git)
cd dwindle-url-shortener

```

---

### 3. Start Containers

```

docker compose up --build

```

---

### 4. Open the Application

Dashboard

```

[http://localhost:8000/dashboard](http://localhost:8000/dashboard)

```

Analytics

```

[http://localhost:8000/analytics-page](http://localhost:8000/analytics-page)

```

API Documentation

```

[http://localhost:8000/docs](http://localhost:8000/docs)

```

---

# Option 2 – Run Locally (Development)

### 1. Create Virtual Environment

```

python -m venv venv

```

Activate it

Windows

```

venv\Scripts\activate

```

Mac / Linux

```

source venv/bin/activate

```

---

### 2. Install Dependencies

```

pip install -r requirements.txt

```

---

### 3. Run the Server

```

uvicorn app.main:app --reload

```

---

### 4. Open the Dashboard

```

[http://127.0.0.1:8000/dashboard](http://127.0.0.1:8000/dashboard)

```

---

# Database Migrations

Alembic is used for managing database schema changes.

Create migration

```

alembic revision --autogenerate -m "migration message"

```

Apply migrations

```

alembic upgrade head

```

---

# API Endpoints

## Create Short URL

```

POST /shorten

```

Example request

```

{
"url": "[https://example.com](https://example.com)",
"custom_code": "optional"
}

```

---

## Redirect Short URL

```

GET /{short_code}

```

---

## List All URLs

```

GET /urls

```

---

## Get Analytics

```

GET /analytics/{short_code}

```

---

# Screenshots

## Dashboard

(Add screenshot here)

## Analytics

(Add screenshot here)

---

# Future Improvements

Possible improvements:

- Click history over time
- Top performing links
- Country-based analytics
- User authentication
- Browser extension
- Public API access

---

# Author

**Sreehari S Kumar**  
BTech IT – CUSAT  

Interested in backend engineering, DevOps, and system design.

---

# License

MIT License
```

---
