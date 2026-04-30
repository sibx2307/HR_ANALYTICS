from flask import Flask, jsonify
from services.analytics import run_anomaly_detection

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "HR Analytics API Running 🚀"}

@app.route("/anomalies", methods=["GET"])
def anomalies():
    data = run_anomaly_detection()
    return jsonify(data.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)