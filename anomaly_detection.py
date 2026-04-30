import pandas as pd
from sklearn.ensemble import IsolationForest
from db.db_connection import get_engine

engine = get_engine()

# Load data
attendance = pd.read_sql("SELECT * FROM attendance", engine)
performance = pd.read_sql("SELECT * FROM performance", engine)
employees = pd.read_sql("SELECT * FROM employees", engine)

# Aggregate
att_summary = attendance.groupby("employee_id").agg({
    "hours_worked": "mean"
}).reset_index()

perf_summary = performance.groupby("employee_id").agg({
    "rating": "mean"
}).reset_index()

# Merge
df = att_summary.merge(perf_summary, on="employee_id")
df = df.merge(employees, left_on="employee_id", right_on="id")

# Features
features = df[["hours_worked", "rating", "salary"]]

# Model
model = IsolationForest(contamination=0.25)
df["anomaly"] = model.fit_predict(features)

df["anomaly_flag"] = df["anomaly"].apply(lambda x: 1 if x == -1 else 0)

print(df[["employee_id", "name", "hours_worked", "rating", "salary", "anomaly_flag"]])