import sqlite3
import pandas as pd
import os

def load_csv_to_sqlite():
    csv_path = os.path.join('data', 'raw', 'customers_raw.csv')
    db_path = os.path.join('data', 'db', 'analytics.db')
    
    df = pd.read_csv(csv_path)
    
    conn = sqlite3.connect(db_path)
    
    df.to_sql('customers_raw', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
    
    print(f"Loaded {len(df)} rows into {db_path}")

if __name__ == "__main__":
    load_csv_to_sqlite()
