# N1 დავალება--------------------------------------------------

# n = int(input("შეიყვანეთ რიცხვი n: "))

# s = 0
# for i in range(1, n + 1):
#     s += i

# print("ჯამი არის:", s)


# N2 დავალება--------------------------------------------------

# import time

# n = int(input("შეიყვანეთ რიცხვი: "))

# while n > 0:
#     print(n)

#     time.sleep(0.09)

#     n -= 1

# N3 დავალება--------------------------------------------------

# from random import randint

# num = randint(1, 100)
# guess = 0
# step = 1

# print("Guess the number between 1 and 100!")

# while guess != num:
#     guess = int(input(f"Step #{step}. Your guess: "))

#     if guess > num:
#         print("Too great\n")
#     elif guess < num:
#         print("Too less\n")

#     step += 1

# print(f"გილოცავთ! თქვენ გამოიცანით რიცხვი: {num}")
# print("თამაში დასრულდა ")

# N4 დავალება--------------------------------------------------

# total_sum = 0

# while True:
#     user_input = input("შეიყვანეთ რიცხვი ან 'sum' დასასრულებლად: ")

#     if user_input == "sum":
#         break

#     if user_input.isdigit():
#         number = int(user_input)
#         if number > 0:
#             total_sum += number
#         else:
#             print("მხოლოდ დადებითი რიცხვები დაითვლება.\n")
#     else:
#         print("გთხოვთ შეიყვანოთ მხოლოდ ნატურალური რიცხვი ან 'sum'.\n")

# print(f"\nდადებითი რიცხვების ჯამი არის: {total_sum}")











