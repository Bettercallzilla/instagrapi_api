from flask import Flask, request, jsonify
from instagpy import InstaGPy

app = Flask(__name__)
insta = InstaGPy()

@app.route('/profile', methods=['GET'])
def get_profile():
    username = request.args.get('username')
    if not username:
        return jsonify({'error': 'Missing "username" parameter'}), 400
    try:
        data = insta.get_user_basic_details(username, pretty_print=False)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055)
