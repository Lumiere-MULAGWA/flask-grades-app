# from flask import Flask, request, jsonify, render_template
# import requests

# app = Flask(__name__)

# # URL du service d'inscription des étudiants
# STUDENT_SERVICE_URL = "http://127.0.0.1:5000"
# grades_by_course = {}  # Format : {course: {student_id: grade}}

# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route pour afficher les étudiants et leurs cotes
# @app.route('/grades', methods=['GET'])
# def get_grades():
#     # Récupérer la liste des étudiants depuis le service flask-student-app
#     response = requests.get(f"{STUDENT_SERVICE_URL}/students")
#     if response.status_code == 200:
#         students = response.json()
#         for student in students:
#             student_id = student['id']
#             student['grades'] = grades_by_course.get(student_id, {})
#         return render_template('grades_list.html', students=students)
#     else:
#         return jsonify({'error': 'Unable to fetch students'}), 500

# # Route pour afficher les cours et les étudiants inscrits
# @app.route('/courses', methods=['GET'])
# def get_courses():
#     # Préparer les données pour afficher les cours et les étudiants inscrits
#     response = requests.get(f"{STUDENT_SERVICE_URL}/students")
#     if response.status_code == 200:
#         students = response.json()
#         courses_data = {}
#         for course, students_grades in grades_by_course.items():
#             courses_data[course] = []
#             for student_id, grade in students_grades.items():
#                 student = next((s for s in students if s['id'] == student_id), None)
#                 if student:
#                     courses_data[course].append({
#                         'id': student['id'],
#                         'name': student['name'],
#                         'email': student['email'],
#                         'faculty': student['faculty'],
#                         'grade': grade
#                     })
#         return render_template('courses_list.html', courses=courses_data)
#     else:
#         return jsonify({'error': 'Unable to fetch students'}), 500

# # Route pour attribuer une cote à un étudiant
# @app.route('/grades/<int:student_id>', methods=['GET', 'POST'])
# def assign_grade(student_id):
#     if request.method == 'POST':
#         course = request.form.get('course')
#         grade = request.form.get('grade')

#         if not course or not grade:
#             return render_template('assign_grade.html', error='Course and grade are required', student_id=student_id)

#         # Vérifier si l'étudiant existe dans le service flask-student-app
#         response = requests.get(f"{STUDENT_SERVICE_URL}/students/{student_id}")
#         if response.status_code == 200:
#             # Ajouter ou mettre à jour la cote pour le cours
#             if course not in grades_by_course:
#                 grades_by_course[course] = {}
#             grades_by_course[course][student_id] = grade
#             return render_template('assign_grade.html', message=f'Grade {grade} assigned for course {course}', student_id=student_id)
#         else:
#             return render_template('assign_grade.html', error='Student not found', student_id=student_id)

#     return render_template('assign_grade.html', student_id=student_id)

# @app.route('/courses/<course_name>/add_student', methods=['GET', 'POST'])
# def add_student_to_course(course_name):
#     # Récupérer la liste des étudiants depuis le service flask-student-app
#     response = requests.get(f"{STUDENT_SERVICE_URL}/students")
#     if response.status_code != 200:
#         return jsonify({'error': 'Unable to fetch students'}), 500

#     students = response.json()

#     if request.method == 'POST':
#         student_id = request.form.get('student_id')
#         grade = request.form.get('grade')

#         if not student_id or not grade:
#             return render_template('add_student_to_course.html', error='Student and grade are required', course_name=course_name, students=students)

#         # Ajouter l'étudiant au cours
#         if course_name not in grades_by_course:
#             grades_by_course[course_name] = {}
#         grades_by_course[course_name][int(student_id)] = grade

#         return render_template('add_student_to_course.html', message=f'Student {student_id} added to course {course_name} with grade {grade}', course_name=course_name, students=students)

#     return render_template('add_student_to_course.html', course_name=course_name, students=students)

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# URL du service d'inscription des étudiants
STUDENT_SERVICE_URL = "http://127.0.0.1:5000"
grades_by_course = {
    "Mathematics": {},
    "Physics": {},
    "Computer Science": {}
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/grades', methods=['GET'])
def get_all_grades():
    response = {}
    for course_name, course_grades in grades_by_course.items():
        response[course_name] = []
        for student_id, grade in course_grades.items():
            response[course_name].append({
                'student_id': student_id,
                'grade': grade
            })
            print(f"Course {course_name} student: {student_id} with grade {grade}")
    if not response:    
        print(f"Error: No grades found")
        return jsonify({'message': 'No grades found'}), 404
    print(f"Grades data: {response}")
    return jsonify(response), 200
# Route pour afficher les étudiants et leurs cotes
@app.route('/grades', methods=['GET'])
def get_grades():
    response = requests.get(f"{STUDENT_SERVICE_URL}/students")
    if response.status_code == 200:
        students = response.json()
        for student in students:
            student_id = student['id']
            student['grades'] = grades_by_course.get(student_id, {})
            print(f"Student {student_id} grades: {student['grades']}")
        if not students:
            print(f"Error: No students found")
            return render_template('grades_list.html', message='No students found')
        return render_template('grades_list.html', students=students)
    else:
        return jsonify({'error': 'Unable to fetch students'}), 500

# Route pour afficher les cours et les étudiants inscrits
@app.route('/courses', methods=['GET'])
def get_courses():
    response = requests.get(f"{STUDENT_SERVICE_URL}/students")
    if response.status_code == 200:
        students = response.json()
        courses_data = {}
        for course, students_grades in grades_by_course.items():
            courses_data[course] = []
            for student_id, grade in students_grades.items():
                student = next((s for s in students if s['id'] == student_id), None)
                if student:
                    courses_data[course].append({
                        'id': student['id'],
                        'name': student['name'],
                        'email': student['email'],
                        'faculty': student['faculty'],
                        'grade': grade
                    })
                    print(f"Course {course} student: {student['name']} with grade {grade}")

        # Vérifier si des cours sont disponibles
        # Si aucun cours n'est trouvé, afficher un message

        if not courses_data:
            print(f"Error: No courses found")
            return render_template('courses_list.html', message='No courses found')
        print(f"Courses data: {courses_data}")
        # Afficher les cours et les étudiants inscrits
        return render_template('courses_list.html', courses=courses_data)
    else:
        return jsonify({'error': 'Unable to fetch students'}), 500

# Route pour ajouter un étudiant à un cours
@app.route('/courses/<course_name>/add_student', methods=['GET', 'POST'])
def add_student_to_course(course_name):
    response = requests.get(f"{STUDENT_SERVICE_URL}/students")
    if response.status_code != 200:
        return jsonify({'error': 'Unable to fetch students'}), 500

    students = response.json()

    if request.method == 'POST':
        student_id = request.form.get('student_id')
        grade = request.form.get('grade')

        if not student_id or not grade:
            print(f"Error: Student ID or grade not provided")
            return render_template('add_student_to_course.html', error='Student and grade are required', course_name=course_name, students=students)

        if course_name not in grades_by_course:
            grades_by_course[course_name] = {}
            print(f"Course {course_name} created")
        # Ajouter l'étudiant au cours
        grades_by_course[course_name][int(student_id)] = grade
        print(f"Student {student_id} added to course {course_name} with grade {grade}")
        # Afficher un message de succès

        return render_template('add_student_to_course.html', message=f'Student {student_id} added to course {course_name} with grade {grade}', course_name=course_name, students=students)
    print(f"Displaying students for course {course_name}")
    # Afficher le formulaire d'ajout d'étudiant au cours
    return render_template('add_student_to_course.html', course_name=course_name, students=students)

if __name__ == '__main__':
    app.run(debug=True, port=5001)