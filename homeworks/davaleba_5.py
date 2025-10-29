# N1 დავალება--------------------------------------------------

# arr = []

# while True:
#     command = input("შეიყვანე ბრძანება (a – დამატება, r – წაშლა, e – გასვლა): ")

#     if command == 'a':
#         value = input("შეიყვანე რიცხვი დასამატებლად: ")
#         arr.append(value)
#     elif command == 'r':
#         value = input("შეიყვანე რიცხვი წასაშლელად: ")
#         if value in arr:
#             arr.remove(value)
#         else:
#             print("ეს რიცხვი სიაში არ არის.")
#     elif command == 'e':
#         break
#     else:
#         print("არასწორი ბრძანება.")

# print("სიის საბოლოო მდგომარეობა:", arr)

# N2 დავალება--------------------------------------------------

# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# print("210-ის ინდექსი:", my_list_1.index(210))

# my_list_1[-1].append("hello")

# del my_list_1[2]
# print("სიიდან წაშლის შემდეგ:", my_list_1)

# my_list_2 = my_list_1.copy()
# my_list_2.clear()

# print("ორიგინალი სია:", my_list_1)
# print("გასუფთავებული ასლი:", my_list_2)

# N3 დავალება--------------------------------------------------

# import re

# number = input("შეიყვანე ტელეფონის ნომერი ფორმატით (123) 456-789: ")

# pattern = r"\(\d{3}\) \d{3}-\d{3}"

# if re.fullmatch(pattern, number):
#     print("ნომერი სწორია:", number)
# else:
#     print("ფორმატი არასწორია")










