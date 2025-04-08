from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "KubeCart is live on EKS!"})

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
