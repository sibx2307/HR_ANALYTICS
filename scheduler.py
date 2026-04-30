import schedule
import time
import subprocess

def job():
    print("⏰ Running ETL...")
    subprocess.run(["python", "etl.py"])

    print("🤖 Running Anomaly Detection...")
    subprocess.run(["python", "main.py"])  # or analytics call

    print("✅ Done")

# Run every day at 9 AM
schedule.every().day.at("09:00").do(job)

print("🚀 Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)