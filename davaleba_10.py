# N1 დავალება--------------------------------------------------

# def ziped(integer,string):
  
#     return [f"({i},{n})"for i,n in list(zip(integer,string))]

# integer = [1,2,3]
# string = ["a","b","c"]

# print(ziped(integer,string))

# N2 დავალება--------------------------------------------------

# from functools import reduce

# def multiply(numbers): 
#     try:
#         product = int(reduce(lambda x,y : x * y ,numbers))
#         return product
#     except TypeError as ex:
#         print(ex)
#     except ValueError as x:
#         print(x)

# excperiment = multiply([1, 2, 3, 4, 5])

# print(excperiment)

# N3 დავალება--------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7]

# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# print(odd_numbers)

# N4 დავალება--------------------------------------------------

# try:
#     lst5 = input("Enter Sequence of Words: ").split()
#     word = input("Enter Ending to match: ")
#     filtered1 = list(filter(lambda x: x.endswith(word), lst5))
# except TypeError:
#     print("Wrong type of input!")
# else:
#     print(filtered1)



