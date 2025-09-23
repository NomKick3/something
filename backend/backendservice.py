from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/api/info', methods=['GET'])
def get_info():
    info_data = {
        "version": "1.0.0",
        "status": "running",
        "description": "Backend service providing information."
    }
    return jsonify(info_data)

if __name__ == '__main__':
    app.run(debug=True)