import os, csv


def create_csv_file():
  path = "CSV"
  filename = "students.csv"

  os.makedirs(path, exist_ok=True)
  filename = os.path.join(path, filename)     

  try:
    with open(filename, mode='x', encoding='utf-8'):
      ...
  except FileExistsError:
    ...

  return filename    


def write_data_to_csv(path: str, data: list):
  with open(path, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())

    data.sort(key=lambda x: int(x['id']))

    writer.writeheader()
    writer.writerows(data)


def read_from_csv(path, st_name='') -> list | str:
  with open(path, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    if st_name:
      return [st for st in reader if st['name'].lower() == st_name.lower()] or f"Student with name '{st_name}' not found"
    
    return [st for st in reader]


def average_marks(path):
  data = read_from_csv(path)
  subjects = set([row['subject_name'] for row in data])
  avgs = {}

  for subject in subjects:
    sum_marks = 0
    quantity = 0

    for row in data:
      if subject == row['subject_name']:
        sum_marks += int(row['mark'])
        quantity += 1
    
    avgs[subject] = round(sum_marks / quantity, 2)

  return avgs


def update_csv_file(path, id, subject, mark):
  students = read_from_csv(path)

  for student in students:
    if id == int(student['id']) and subject.lower() == student['subject_name'].lower():
      student['mark'] = mark

      break
  else:
    print("Can't update")

    return
  
  write_data_to_csv(path, students)


def add_data_to_csv(path: str, student: dict):
  students = read_from_csv(path)

  for row in students:
    if int(row['id']) == student['id']:
      print(f"Student with ID '{row['id']}' already exists...")
      break
  else:
    students.append(student)

    write_data_to_csv(path, students)


def show_data(path: str, st_name=''):
  data = read_from_csv(path, st_name)

  if type(data) != list:
    print(data)
    
    return

  w_id = 7
  w_name = 12
  w_age = 7
  w_grade = 7
  w_subject_name = 20
  lines = sum((2, w_id, 1, w_name, 1, w_age, 1, w_grade, 1, w_subject_name, 1, 6))

  print("\nStudents info:\n")


  print("=" * lines)

  head = tuple(data[0].keys())  

  print(
    f"  {head[0]:<{w_id}}",
    f"{head[1]:<{w_name}}",
    f"{head[2]:<{w_age}}",
    f"{head[3]:<{w_grade}}",
    f"{head[4]:<{w_subject_name}}",
    f"{head[5]}",
  )

  print("=" * lines)



  for row in data:
    print(
      f"  {row['id']:<{w_id}}",
      f"{row['name']:<{w_name}}",
      f"{row['age']:<{w_age}}",
      f"{row['grade']:<{w_grade}}",
      f"{row['subject_name']:<{w_subject_name}}",
      f"{row['mark']}",
    )
    
    print("-" * lines)