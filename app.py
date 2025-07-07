from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data
USER = {
    "name": "Kunal Nawaria",
    "mobile_number": "8949270667"
}

@app.route('/get-user', methods=['GET'])
def get_user():
    return jsonify({
        "status": "success",
        "user": USER
    })

if __name__ == '__main__':
    app.run(debug=True)
