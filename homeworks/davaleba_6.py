my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}
students_id = [str(student["id"]) for student in my_dict["students"]]
print("studentebis ID:", ", ".join(students_id))
print("=" * 45)
user_input = input("Enter student ID: ")

if user_input in students_id:
    for student_ in my_dict.get("students"):
        if str(student_["id"]) == user_input:
            st_name = student_["name"]
            st_age = student_["age"]
            for grade in my_dict.get("subjects"):
                st_subject = grade["name"]
                st_grade = grade["grades"].get(user_input)


                print(f"Name: {st_name}, Age: {st_age}, Subject: {st_subject}, Grade: {st_grade}")
            print('-' * 45)
else:
    print("That Student ID does not exist")




















