from flask import Flask, jsonify
from database import get_db_connection
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test-db")
def test_db():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM medicines")
        medicines = cursor.fetchall()

        return jsonify({
            "status": "success",
            "message": "MySQL connected successfully!",
            "medicines": medicines
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    app.run(debug=True)