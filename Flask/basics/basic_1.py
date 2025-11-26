from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return "Server is running", 200


@app.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword", default=None)
    limit = request.args.get("limit", default=10, type=int)
    if keyword is None:
        return "Give the keyword to search", 404
    return jsonify(
        {"message": "Got the request", "data": f"{keyword}: showing {limit} data"}
    ), 200


@app.route("/data", methods=["POST"])
def data():
    data = request.get_json()
    title = data.get("title")
    return f"got {title} as json", 200


if __name__ == "__main__":
    app.run(debug=True)
