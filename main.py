from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get_user/<user_id>")
def get_user(user_id):
    return "user" + user_id


@app.route("/create_user/", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 200


if __name__ == "__main__":
    app.run()
