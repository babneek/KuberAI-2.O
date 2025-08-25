from database import SessionLocal, Investment
import os
import sqlite3

def show_all_investments():
    session = SessionLocal()
    investments = session.query(Investment).all()
    if investments:
        for inv in investments:
            print(inv.username, inv.amount, inv.gold_price, inv.weight, inv.invested_at)
    else:
        print("No investments found.")
    session.close()

def show_all_investments_sqlite():
    db_path = os.path.join(os.path.dirname(__file__), "data", "gold_investments.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM investments")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No investments found.")
    conn.close()

db_path = os.path.join(os.path.dirname(__file__), "data", "gold_investments.db")
print("Using DB:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List all tables in the database
print("Tables in DB:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)

# Check if 'investments' table exists and show its contents
if any('investments' in t for t in tables):
    print("\nRows in 'investments' table:")
    cursor.execute("SELECT * FROM investments")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No investments found.")
else:
    print("'investments' table does not exist.")

conn.close()

if __name__ == "__main__":
    show_all_investments()
    show_all_investments_sqlite()