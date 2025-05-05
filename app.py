import os

from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/') 
def home():
    return "John Philip Pargan BSIT - 3 B"

if __name__ == "__main__":
   app.run(host="0.0.0.0",
           port= int(os.environ.get("PORT", 8000)))
