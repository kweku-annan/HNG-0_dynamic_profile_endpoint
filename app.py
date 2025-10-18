import os

from flask import Flask, jsonify, redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    # Redirects to the '/me' route
    return redirect(url_for('me'), code=301)

@app.route('/me', methods=['GET'])
def me():
    from models.profile import Profile
    profile = Profile()
    data = profile.profile_dict()
    # print(data)
    return jsonify(data), 200

# For Local testing

# if __name__ == "__main__":
#     # Get port from environment variable.
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port, debug=True)