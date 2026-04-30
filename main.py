import schedule
import time
import subprocess

def job():
    subprocess.run(["python", "etl.py"])

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)