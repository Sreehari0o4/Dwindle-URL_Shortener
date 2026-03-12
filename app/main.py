from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse, FileResponse
from datetime import datetime, timedelta
import random
import string

from .database import engine, Base, get_db
from .models import URL
from .schemas import URLRequest
from .cache import redis_client


app = FastAPI()


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# ---------------- HOME ----------------

@app.get("/")
def home():
    return {"message": "URL Shortener API running"}


# ---------------- DASHBOARD ----------------

@app.get("/dashboard")
def dashboard():
    return FileResponse("frontend/index.html")


# ---------------- ANALYTICS PAGE ----------------

@app.get("/analytics-page")
def analytics_page():
    return FileResponse("frontend/analytics.html")


# ---------------- CREATE SHORT URL ----------------

@app.post("/shorten")
def shorten_url(request: URLRequest, db: Session = Depends(get_db)):

    if request.custom_code:
        short_code = request.custom_code
    else:
        short_code = generate_short_code()

    existing = db.query(URL).filter(URL.short_code == short_code).first()

    if existing:
        return {"error": "Short code already exists"}

    expires_at = None

    if request.expires_in_hours:
        expires_at = datetime.utcnow() + timedelta(hours=request.expires_in_hours)

    new_url = URL(
        original_url=request.url,
        short_code=short_code,
        expires_at=expires_at
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}"
    }


# ---------------- LIST ALL URLS ----------------

@app.get("/urls")
def list_urls(db: Session = Depends(get_db)):

    urls = db.query(URL).all()

    result = []

    for url in urls:
        result.append({
            "short_code": url.short_code,
            "original_url": url.original_url,
            "clicks": url.clicks
        })

    return result


# ---------------- ANALYTICS FOR ONE LINK ----------------

@app.get("/analytics/{short_code}")
def get_analytics(short_code: str, db: Session = Depends(get_db)):

    url = db.query(URL).filter(URL.short_code == short_code).first()

    if url:
        return {
            "original_url": url.original_url,
            "clicks": url.clicks
        }

    return {"error": "URL not found"}


# ---------------- REDIRECT (KEEP LAST) ----------------

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):

    cached_url = redis_client.get(short_code)

    # Cache hit
    if cached_url:
        url = db.query(URL).filter(URL.short_code == short_code).first()
        if url:
            url.clicks += 1
            db.commit()
        return RedirectResponse(cached_url)

    # Cache miss
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        return {"error": "URL not found"}

    if url.expires_at and datetime.utcnow() > url.expires_at:
        return {"error": "URL expired"}

    redis_client.set(short_code, url.original_url)

    url.clicks += 1
    db.commit()

    return RedirectResponse(url.original_url)