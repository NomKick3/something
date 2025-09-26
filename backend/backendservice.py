import time
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
start_time = time.time()

def get_db_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="examplepassword",
        host="postgres",
        port="5432"
    )

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1;")
            quote = cursor.fetchone()
            if quote:
                return jsonify({"id": quote[0], "quote": quote[1]})
            return jsonify({"error": "No quotes found"}), 404

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