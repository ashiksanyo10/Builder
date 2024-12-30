from flask import Flask, request, jsonify
import mysql.connector
import json

# Load config
with open('config.json', 'r') as f:
    config = json.load(f)

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

@app.route('/check', methods=['POST'])
def check_duplicate():
    data = request.json
    gti = data["gti"]
    task_id = data["task_id"]

    conn = get_db_connection()
    cursor = conn.cursor()

    # Check for duplicate
    cursor.execute("SELECT rowid, task_id FROM content_table WHERE gti = %s", (gti,))
    result = cursor.fetchone()

    if result:
        rowid, old_task_id = result
        # Log in duplicate_log
        cursor.execute("INSERT INTO duplicate_log (gti, old_task_id, new_task_id) VALUES (%s, %s, %s)", (gti, old_task_id, task_id))
        conn.commit()
        return jsonify({"status": "duplicate", "rowid": rowid, "old_task_id": old_task_id})
    else:
        # Insert new record
        cursor.execute("INSERT INTO content_table (gti, task_id) VALUES (%s, %s)", (gti, task_id))
        conn.commit()
        return jsonify({"status": "not_duplicate"})

if __name__ == "__main__":
    app.run(port=5000)
