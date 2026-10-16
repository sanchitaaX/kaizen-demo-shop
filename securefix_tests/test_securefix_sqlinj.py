import sqlite3
import pytest
from shop.db import find_customer

def _setup_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE customers (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT,
        tier TEXT
    )""")
    conn.execute("INSERT INTO customers (username, email, tier) VALUES ('alice', 'alice@example.com', 'gold')")
    conn.commit()
    return conn

def test_find_customer_sql_injection():
    conn = _setup_db()
    # Benign lookup should succeed
    rows = find_customer(conn, "alice")
    assert len(rows) == 1, "Benign lookup should return exactly one row"
    # Injection attempt should return no rows
    malicious = "alice' OR '1'='1"
    rows = find_customer(conn, malicious)
    assert rows == [], f"SQL injection should not return any rows, got {rows}"