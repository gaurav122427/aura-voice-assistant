from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    # temporary test response
    return jsonify({
        "answer": f"You asked: {question}"
    })

if __name__ == "__main__":
    app.run(port=8000, debug=True)