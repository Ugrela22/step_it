# N1 დავალება--------------------------------------------------

# int_list = [10, 20, 30, 40]

# def add_number(n):
#     global int_list
#     int_list.append(n)

# add_number(15)
# print(int_list)

# N2 დავალება--------------------------------------------------

# def sum_list(numbers):
#     return sum(numbers)

# nums = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# result = sum_list(nums)

# print("სიის ჯამი არის:", result)

# N3 დავალება--------------------------------------------------

# gl_str = "Global"

# def test_func():
#     gl_str = "Local" 
#     return gl_str     

# print(test_func())   
# print(gl_str)      

# N4 დავალება--------------------------------------------------

# def recursive(number, total=0):

#     if number == 0:
#         print(total)
#     else:
#         digit = number % 10  
#         recursive(number // 10, total + digit)  

# num = int(input("შეიყვანეთ რიცხვი: "))
# recursive(num)
 
# N5 დავალება--------------------------------------------------

# def recursive(lst, reversed_str=''):
#     if not lst:  
#         print(reversed_str)
#     else:
#         char = lst.pop()            
#         recursive(lst, reversed_str + char)  

# string = input("შეიყვანეთ ტექსტი: ")
# recursive(list(string))  
















