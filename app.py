from flask import Flask, jsonify

profile = {
    "status": "success",
    "user": {
        "email": "kwekuannan.dev@gmail.com",
        "name": "Emmanuel Adu Saah",
        "stack": ["Python", "Django", "Flask"]
    },
    "timestamp": "Friday October 17, 2025. 4:38:17UTC",
    "fact": "Cats sleep a lot!"
}

app = Flask(__name__)

@app.route('/me')
def home():
    return jsonify(profile)


if __name__ == "__main__":
    app.run(debug=True)