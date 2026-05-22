# CashTrack — Cashback Deal Tracker

A full-stack web application to track cashback deals across e-commerce platforms. Add deals, calculate savings automatically, mark them as redeemed, and monitor your total cashback earned.

> Built with Flask (REST API) + SQLite + Vanilla JS frontend.

---

## 🖥️ Demo

<!-- Add your Render URL here after deployment -->
**Live:** [cashtrack-nect.onrender.com](https://cashtrack-nect.onrender.com)

![CashTrack Screenshot](screenshot.png)

---

## ✨ Features

- Add cashback deals with store name, original price, cashback %, and deal URL
- Automatic savings calculation per deal
- Mark deals as redeemed — tracks total cashback earned
- Filter deals by All / Active / Redeemed
- Live stats bar — total deals, redeemed count, total savings
- Fully persistent storage via SQLite
- REST API with 5 endpoints following HTTP conventions

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask, Flask-CORS |
| Database | SQLite |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Architecture | REST API + SPA (Single Page Application) |
| Deployment | Render |

---

## 📡 API Reference

Base URL: `http://localhost:5000/api`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/deals` | Fetch all deals |
| `POST` | `/deals` | Add a new deal |
| `PUT` | `/deals/:id` | Mark a deal as redeemed |
| `DELETE` | `/deals/:id` | Delete a deal |
| `GET` | `/deals/stats` | Get total savings & redeemed count |

### Example Requests

**Add a deal**
```bash
curl -X POST http://localhost:5000/api/deals \
  -H "Content-Type: application/json" \
  -d '{
    "store": "Amazon",
    "cashback_percent": 5,
    "original_price": 2000,
    "deal_url": "https://amazon.in"
  }'
```

**Get all deals**
```bash
curl http://localhost:5000/api/deals
```

**Get savings stats**
```bash
curl http://localhost:5000/api/deals/stats
```

**Response format**
```json
[
  {
    "id": 1,
    "store": "Amazon",
    "cashback_percent": 5.0,
    "original_price": 2000.0,
    "deal_url": "https://amazon.in",
    "redeemed": 0,
    "created_at": "2026-05-22 10:15:00"
  }
]
```

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/cashtrack.git
cd cashtrack
```

**2. Install dependencies**
```bash
pip install flask flask-cors
```

**3. Start the server**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

The SQLite database (`deals.db`) is created automatically on first run.

---

## 📁 Project Structure

```
cashtrack/
├── app.py              # Flask app entry point
├── database.py         # DB connection & schema init
├── deals.db            # SQLite database (auto-created)
├── templates/
│   └── index.html      # Frontend SPA
└── routes/
    ├── __init__.py
    └── deals.py        # API route handlers (Blueprint)
```

---

## 💡 Design Decisions

- **Flask Blueprints** — routes are modularised into a separate `deals` blueprint, keeping `app.py` clean and scalable
- **SQLite** — lightweight and zero-config for development; would replace with PostgreSQL in production
- **CORS enabled** — allows frontend and backend to run on different origins, standard in real-world deployments
- **`row_factory = sqlite3.Row`** — returns query results as dict-like objects for clean JSON serialisation
- **REST conventions** — GET for reads, POST for creates, PUT for updates, DELETE for removes; correct HTTP status codes returned

---

## 🔮 What I'd Add Next

- User authentication (JWT)
- PostgreSQL + SQLAlchemy for production DB
- Redis caching for the deals list
- Deal expiry dates with auto-archiving
- Browser notifications for expiring deals

---

## 👤 Author

**Dinesh Karthik T**
[GitHub](https://github.com/Dineshkarthik2906) · [LinkedIn](https://linkedin.com/in/dinesh-karthik-2400a8286)
