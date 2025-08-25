# KuberAI-2.O

KuberAI-2.O is a Streamlit-based financial assistant that helps users learn about and invest in digital gold.  
It features a chatbot, investment suggestions, and a secure backend using FastAPI and SQLite.

## Features

- 💬 **Kuber AI Chatbot**: Ask financial questions and get instant answers.
- 🪙 **Digital Gold Investment**: Invest in 24k 99.99% pure gold securely.
- 📊 **Investment History**: All investments are saved in a local SQLite database.
- 🔒 **Secure & Private**: Your data is stored locally and never shared.

## Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: FastAPI (Python)
- **Database**: SQLite (via SQLAlchemy)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/babneek/KuberAI-2.O.git
cd KuberAI-2.O
```

### 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start the backend

```bash
cd backend
uvicorn main:app --reload
```

### 4. Start the frontend

```bash
cd ../frontend
streamlit run app.py
```

## Accessing the Database

The investment records are stored in a SQLite database file located at:

```
backend/data/gold_investments.db
```

### To view or query the database:

#### **Option 1: Using Python**

Simply run the following script from the `backend` folder:

```bash
python check_db.py
```

This will print all investment records from the database.

#### **Option 2: Using DB Browser for SQLite**

1. Download [DB Browser for SQLite](https://sqlitebrowser.org/).
2. Open `backend/data/gold_investments.db`.
3. Browse and export your investment data.

---

## Folder Structure

```
KUBERAI-2.O/
├── .venv/
├── backend/
│   ├── __pycache__/
│   ├── data/
│   │   └── gold_investments.db
│   ├── check_db.py
│   ├── database.py
│   ├── main.py
│   ├── model.py
│   └── service.py
├── frontend/
│   ├── assets/
│   ├── pages/
│   │   ├── 1_login.py
│   │   ├── 2_welcome.py
│   │   ├── 3_chat.py
│   │   └── 4_invest.py
│   └── app.py
├── .env
├── README.md
└── requirements.txt
```

## License

MIT

---

**Made with ❤️ by [Your Name]**