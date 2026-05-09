import sqlite3
import os

def city_kpi(city: str):
    db_path = os.path.join('data', 'db', 'analytics.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = """
    SELECT 
        COUNT(*) as total_customers,
        AVG(monthly_spend) as avg_monthly_spend,
        SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) as churned_customers,
        ROUND(SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as churn_rate_pct
    FROM customers_raw 
    WHERE city = ?
    """
    
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result and result[0] > 0:
        print(f"KPI for {city}:")
        print(f"  Total Customers: {result[0]}")
        print(f"  Avg Monthly Spend: ${result[1]:.2f}")
        print(f"  Churned Customers: {result[2]}")
        print(f"  Churn Rate: {result[3]}%")
    else:
        print(f"No data found for city: {city}")

if __name__ == "__main__":
    print("=== Testing Mumbai ===")
    city_kpi("Mumbai")
    
    print("\n=== Testing SQL Injection Attempt ===")
    city_kpi("Mumbai' OR 1=1 --")
