import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

QUOTES = [
    "Simplicity is the soul of efficiency. — Austin Freeman",
    "First, solve the problem. Then, write the code. — John Johnson",
    "Experience is the name everyone gives to their mistakes. — Oscar Wilde",
    "In order to be irreplaceable one must always be different. — Coco Chanel",
    "Java is to JavaScript what car is to Carpet. — Chris Heilmann",
    "Knowledge is power. — Francis Bacon"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/quote")
def get_quote():
    return jsonify({"quote": random.choice(QUOTES)})

@app.route("/api/greet", methods=["POST"])
def greet():
    data = request.get_json() or {}
    name = data.get("name", "stranger").strip()
    if not name:
        name = "stranger"
    return jsonify({"message": f"Hello, {name}! Welcome to your brand new Flask application."})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
