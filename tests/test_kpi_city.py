import pytest
import sqlite3
import pandas as pd
import os
import sys
from io import StringIO
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from kpi_city import city_kpi

@pytest.fixture
def setup_test_db():
    db_path = os.path.join('data', 'db', 'analytics.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    test_data = [
        (1, 'Mumbai', 2500.50, 0),
        (2, 'Mumbai', 3000.00, 1),
        (3, 'Delhi', 1800.75, 0)
    ]
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS customers_raw')
    cursor.execute('''
        CREATE TABLE customers_raw (
            customer_id INTEGER,
            city TEXT,
            monthly_spend REAL,
            churned INTEGER
        )
    ''')
    cursor.executemany('INSERT INTO customers_raw VALUES (?, ?, ?, ?)', test_data)
    conn.commit()
    conn.close()
    
    yield
    
    if os.path.exists(db_path):
        os.remove(db_path)

def test_city_kpi_happy_path(setup_test_db):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        city_kpi("Mumbai")
        output = mock_stdout.getvalue()
    
    assert "KPI for Mumbai" in output
    assert "Total Customers: 2" in output
    assert "Avg Monthly Spend: $2750.25" in output
    assert "Churned Customers: 1" in output
    assert "Churn Rate: 50.0%" in output

def test_city_kpi_sql_injection_attempt(setup_test_db):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        city_kpi("Mumbai' OR 1=1 --")
        output = mock_stdout.getvalue()
    
    assert "No data found for city: Mumbai' OR 1=1 --" in output
    assert "Total Customers: 2" not in output
    assert "Total Customers: 3" not in output
