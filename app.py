from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sahiljain@123",
    database="students"
)

# Define API routes

@app.route("/students", methods=["GET"])
def get_students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    response = [{"id": student[0], "name": student[1], "email": student[2]} for student in students]
    return jsonify(response)

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    if student:
        response = {"id": student[0], "name": student[1], "email": student[2]}
        return jsonify(response)
    else:
        return jsonify({"error": "Student not found"}), 404

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    return jsonify({"success": "Student added successfully"}), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    cursor = db.cursor()
    cursor.execute("UPDATE students SET name = %s, email = %s WHERE id = %s", (name, email, student_id))
    db.commit()
    return jsonify({"success": "Student updated successfully"}), 200

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    db.commit()
    return jsonify({"success": "Student deleted successfully"}), 200

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

