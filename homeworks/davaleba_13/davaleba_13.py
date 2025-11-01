students = [
  {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
  {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
  {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
  {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
  {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
  {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
  {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
]

new_student = {
  'id': 5,
  'name': 'Demetre',
  'age': 18,
  'grade': 'A',
  'subject_name': 'Informatic',
  'mark': 94
}

new_students = [
  {
    'id': 15,
    'name': 'Alexandre',
    'age': 16,
    'grade': 'A',
    'subject_name': 'English',
    'mark': 96
  },
  {
    'id': 27,
    'name': 'Nana',
    'age': 21,
    'grade': 'C',
    'subject_name': 'Physic',
    'mark': 71
  },
]

from for_13 import create_csv_file, write_data_to_csv, read_from_csv, average_marks, update_csv_file, add_data_to_csv, show_data

filename = create_csv_file()

write_data_to_csv(filename, students)

file_content = read_from_csv(filename, 'nino')

if type(file_content) == list:
  for student in file_content:
    print(student)
else:
  print(file_content)

avgs = average_marks(filename)
for k, v in avgs.items():
  print(f"{k:<15}{v}")

update_csv_file(filename, 19, "Mathematic", 89)

add_data_to_csv(filename, new_student)

for new_student in new_students:
  add_data_to_csv(filename, new_student)


show_data(filename)

show_data(filename, "Nino")