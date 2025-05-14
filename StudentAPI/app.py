from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
students = [
    {"id": 1, "name": "Alice", "age": 20, "course": "Math"},
    {"id": 2, "name": "Bob", "age": 22, "course": "Physics"}
]

# GET /students - returns all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# POST /students - adds a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "age", "course")):
        return jsonify({"error": "Missing student data"}), 400

    new_id = students[-1]["id"] + 1 if students else 1
    new_student = {
        "id": new_id,
        "name": data["name"],
        "age": data["age"],
        "course": data["course"]
    }
    students.append(new_student)
    return jsonify(new_student), 201

# GET /students/<id> - returns student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
