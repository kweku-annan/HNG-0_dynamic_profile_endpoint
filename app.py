from datetime import datetime, timezone

from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/me', methods=['GET'])
def me():
    from models.profile import Profile
    profile = Profile()
    data = profile.profile_dict()

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)