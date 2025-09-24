import time
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
start_time = time.time()

@app.route('/api/info', methods=['GET'])
def get_info():
    elapsed_time = int(time.time() - start_time)
    info_data = {
        "version": "1.0.0",
        "status": "running",
        "timer": elapsed_time
    }
    return jsonify(info_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)