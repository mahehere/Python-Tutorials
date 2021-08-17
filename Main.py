# 1.Python calculator program
#
# print("Welcome to Python Calculator")
# print("Enter 1st Number :")
# a = input()
# print("Enter 2nd Number :")
# b = input()
# print("The Result is :", int(a) + int(b))

# 2.Using string datatype and its few functions
#
# mystr = ("usage of string datatype")
# # print(len(mystr))
# # print(mystr[1:25:])
# # print(mystr.upper())
# print(mystr.isalpha())
# print(mystr.capitalize())

# 3. Creating a dictonary and displaying the meaning based on user input
#
# dict = {'value':"it is value of sets",
#         2:"values is changeable like list datatype",
#         'Immutable' : "values that cannot be changed like tuple datatype",
#         'String' : "a python datatype that display chars based on index value",
#         'Index': "starts from 0 in python"}
# print(dict)
# print("Enter the word for which you need details : ")
# a = input()
# print(type(dict))
# del(dict[2])
# d2 = {'New addition':"something that is added with update function"}
# dict.update(d2)
# print(dict[a])
# del dict['value']
# print(dict)

# # 4.Using list datatype
#
# mylist = [1, 2, 'Mahesh', 4]
# print(mylist)
# print(type(mylist))
# mylist.pop()
# print(mylist)
# mylist.append(345)
# print(mylist)
# mylist.remove(2)
# print(mylist)
# mylist.insert(0, "Ashvitha")
# print(mylist)
# mylist.reverse()
# print(mylist)
# mylist.clear()
# print(mylist)

# # 5.Get age details and display results using else, elif statements
#
# print("Please enter your age: ")
# age = int(input())
# # if 8 > age >= 80:
# #     print("Please enter age withing the limit: ")
# if age < 18:
#     print("You are not eligible for driving")
# elif age == 18:
#     print("Please check with officer for eligibility")
# else:
#     print("You are eligible for driving")

#6 Define function and docstring
# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))

# def func1(a, b):
#     """This is a docstring"""
#     int(input("a:"))
#     input("b:")
#     c = a*b
#     return c

#7 Try except exception
# a = int(input("a:"))
# b = input("b: ")
# try:
#     print("The result is : ", a+b)
# except Exception as y:
#     print("The error is :", y)
#
# print("the program must continue")

#print(func1.__doc__)

# try:
#
#     func1(x)
#     func1("Print this twice")
#     print(x)
#
# except:
#     print("Exception handled")

# 8.File I/O basics

# with open("file bas.txt") as f:
#     a = f.readline()
#     # print(a)
#     b = f.tell()
#     print(a)
#     print(b)

# f = open("file bas.txt")
# #f.read()
# #print(f.readlines())
# print(f.readline())
# #cntnt = f.read()
# #print(cntnt)
# f.close()


#0 1 1 2 3 5 8 13 21 34
# def fib_iterative(n):
#     """Testing of fibonacci series"""
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         c = fib_iterative(n-1) + fib_iterative(n-2)
#         return c
#     #print(fib_iterative())
#
# #fac_recursive = lambda n:n
# def fac_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac_recursive(n-1)
#         #print(n * fac_recursive(n-1))
#
#
# num = int(input("Enter the number: "))
# try:
#
#     print("this is iterative answer for Fibonacci series: ", fib_iterative(num))
#     print("this is the recursive answer for factorial: ", fac_recursive(num))
# #print(num)
# #print("The answer is: ", fib_iterative())
# #print(n)
# except Exception as e:
#     print(e)
# print(fib_iterative.__doc__)

#     #
#     # for i in range(n):
#     #     i = i+1
#     #     #return i
#
#
# num = int(input("enter the number: "))
# print("The answer is : ", fib_iterative(num))
# print(fib_iterative().__doc__)

# class Course:
#     def __init__(self,name):
#         self.name = name
#         self.students = []
#
#
# def add_studs(self,student):
#     self.students.append(student)
#
#
#
#input("Enter class")

a = [10,20,"mahesh","sam",30,50,4,6,8,20]  #str(input("enter the letter"))
for i in a:
    #print(i)
    if str(i).isnumeric() and i > 10:
        print(i)



# print(a)
# if a == 's':
#     print("True")
# else:
#     print("False")