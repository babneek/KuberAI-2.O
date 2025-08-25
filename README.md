# KuberAI-2.O

KuberAI-2.O is a Streamlit-based financial assistant that helps users learn about and invest in digital gold.  
It features a chatbot, investment suggestions, and a secure backend using FastAPI and SQLite.

---

## 🚀 Live Demo

Try the app here: [KuberAI-2.O Live Demo](https://kuberai-2o-nrkiiaqurskkptwzjogyty.streamlit.app/login)

---

## Features

- 💬 **Kuber AI Chatbot**: Ask financial questions and get instant answers.
- 🪙 **Digital Gold Investment**: Invest in 24k 99.99% pure gold securely.
- 📊 **Investment History**: All investments are saved in a local SQLite database.
- 🔒 **Secure & Private**: Your data is stored locally and never shared.

## Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI (Python, hosted on Railway)
- **Database:** SQLite (via SQLAlchemy)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/babneek/KuberAI-2.O.git
cd KuberAI-2.O
```

### 2. Install dependencies

#### Frontend
```bash
cd frontend
pip install -r requirements.txt
```

#### Backend
```bash
cd backend
pip install -r requirements.txt
```

### 3. Start backend locally

```bash
cd backend
uvicorn main:app --reload
```

### 4. Start frontend locally

```bash
cd frontend
streamlit run app.py
```

## Accessing the Database

The investment records are stored in a SQLite database file located at:

```
backend/data/gold_investments.db
```

To view or query the database, run:

```bash
python backend/check_db.py
```

Or use DB Browser for SQLite to open `backend/data/gold_investments.db`.

## Folder Structure

```
KUBERAI-2.O/
├── .env
├── backend/
│   ├── data/
│   │   └── gold_investments.db
│   ├── check_db.py
│   ├── database.py
│   ├── main.py
│   ├── model.py
│   ├── requirements.txt
│   └── service.py
├── frontend/
│   ├── assets/
│   ├── pages/
│   │   ├── 1_login.py
│   │   ├── 2_welcome.py
│   │   ├── 3_chat.py
│   │   └── 4_invest.py
│   ├── app.py
│   └── requirements.txt
├── README.md
```

## Environment Variables

- Add your API keys and secrets to the `.env` file in the project root.
- Example:
  ```
  OPENROUTER_API_KEY=your_api_key_here
  ```

## Deployment Notes

- **Frontend** is deployed on Streamlit Cloud.
- **Backend** is deployed on Railway and accessible via a public URL.
- Update frontend API URLs to point to your Railway backend.

## Approach & Challenges

- Modular separation of frontend and backend for maintainability.
- Used SQLAlchemy for robust database management.
- Provided clear instructions and relative asset paths for cloud compatibility.
- **Challenge:** Streamlit Cloud cannot run FastAPI backend locally; backend must be hosted externally.
- **Challenge:** SQLite is not persistent on Streamlit Cloud; consider using a cloud database for production.
- **Note:** Sensitive data should use Streamlit Cloud secrets, not `.env` in public repos.

---

**Made with ❤️ by [Your Name]**