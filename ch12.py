# Python Basics Chapter 12:
# =========================

# 1. Lambda Expression

# anonymous function

# def add(a, b):
#     return a + b

# print(add(2, 3))

# add_lamb = lambda a, b : a + b
# print(add_lamb(2, 3))

# print(add)
# print(add_lamb)

# mul = lambda a, b : a * b
# print(mul(2, 3))

# Used with built in functions like - map, reduce, filter etc.

# 2. Lambda Expression Practice

# def is_even(a):
#     return a % 2 == 0

# print(is_even(2))

# is_even = lambda a : a % 2 == 0
# print(is_even(2))

# def last_char(s):
#     return s[-1]

# print(last_char("Anshul"))

# last_char = lambda s : s[-1]
# print(last_char("Anshul"))

# lambda with if - else :

# def func(s):
#     if len(s) > 5:
#         return True
#     return False

# print(func("Anshul"))

# def func(s):
#     return len(s) > 5

# print(func("Anshul"))

# func = lambda s : True if len(s) > 5 else False
# print(func("Anshul"))

# func = lambda s : len(s) > 5
# print(func("Anshul"))

# Lambda function inside a normal function :

# def func(n):
# 	return lambda a : a**n

# num1, num2 = input("Enter two numbers : ").split()

# print(func(int(num1))(int(num2)))
