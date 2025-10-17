from datetime import datetime, timezone

from flask import Flask, jsonify

profile = {
    "status": "success",
    "user": {
        "email": "kwekuannan.dev@gmail.com",
        "name": "Emmanuel Adu Saah",
        "stack": ["Python", "Django", "Flask"]
    },
    "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'),
    "fact": "Cats sleep a lot!"
}

app = Flask(__name__)

@app.route('/me')
def home():
    return jsonify(profile)


if __name__ == "__main__":
    app.run(debug=True)