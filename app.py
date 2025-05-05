from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "John Philip Pargan BSIT - 3 B"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
