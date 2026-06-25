import csv

students = [
    {"name":"Mercy","grade":85},
    {"name":"Amina","grade":70},
    {"name":"Gray","grade":40}
]

sorted_students = sorted(students, key=lambda s: s["name"],)
for student in sorted_students:
    print(student["name"] + "-" + str(student["grade"]))
