# Applied Analytics Mini Project

A beginner-friendly project demonstrating ETL pipeline, SQL queries with parameterization, and SQL injection protection.

## Project Structure
```
vibe-kpi-demo/
├── data/
│   ├── raw/customers_raw.csv     # Raw customer data
│   └── db/analytics.db           # SQLite database
├── src/
│   ├── etl_load_sqlite.py        # ETL script to load CSV into SQLite
│   └── kpi_city.py               # KPI calculation with SQL injection protection
├── tests/
│   └── test_kpi_city.py          # Pytest tests
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```

## Setup and Run Commands

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run ETL Pipeline
```bash
python src/etl_load_sqlite.py
```

### 3. Run KPI Script
```bash
python src/kpi_city.py
```

### 4. Run Tests
```bash
pytest tests/test_kpi_city.py -v
```

## File Explanations
- `data/raw/customers_raw.csv`: Sample customer data with 12 rows across 4 cities
- `src/etl_load_sqlite.py`: Loads CSV data into SQLite database using pandas
- `src/kpi_city.py`: Calculates city-specific KPIs with parameterized SQL queries
- `tests/test_kpi_city.py`: Tests for happy path and SQL injection protection
- `requirements.txt`: Minimal dependencies (pandas, pytest)
- `.gitignore`: Ignores virtual environment, cache, and database files