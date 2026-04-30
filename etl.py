import pandas as pd
from db.db_connection import get_engine

engine = get_engine()

# Load CSVs
employees = pd.read_csv("data/employees.csv")
attendance = pd.read_csv("data/attendance.csv")
performance = pd.read_csv("data/performance.csv")

# Load into DB
employees.to_sql("employees", engine, if_exists="replace", index=False)
attendance.to_sql("attendance", engine, if_exists="replace", index=False)
performance.to_sql("performance", engine, if_exists="replace", index=False)

print("✅ Data loaded successfully")