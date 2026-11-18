# #frist program on python
# #print("prince upadhyay")
# #print("hello this is prince \n this my frist program \n ihope you like it")
# #this is a firste way to use single line comment
# """this is a second way to write multi line comment
# jaha tak meri bat hai to ye valajada shi hai"""
# #ab padhenge variable
# #a = "prince"
# #print(a) #yha par("") ka use nhi karenge agar karenge to vo print ki value run kare naki variable ka
# #datatypes and user input
# #name =input("enter your name: ")
# #print(name)
# #age = int (input("enter age: "))
# #print(age)
# #length = float(input("enter the length of rectangle: "))
# #print(length)
# #exp1 = eval(input("enter your equation here: "))
# #print(exp1)
# #typecasting and subtypes
# #name = ("jhon")
# #age = 23
# #print(type(name))
# #print(type(age))
# #b = 1.23
# #print(type(a))
# #print(type(b))
# #a = int(a)
# #print("after conversion",type(a))
# # = a+b
# #print(c)
# #print(type(c))
# """problem solving"""
# #write a program to dispaly a person's name,age and address in three different lines
# # name = "jhon" 
# # age = 23
# # address = "ludhiana"
# # print(name)
# # print(age)
# # print(address)
# #write a program to swap to variables.
# # x = 12
# # y = 16
# # temp = x
# # print(temp)
# # x = y
# # print (x)
# # y = temp
# # print(y)
# # print("value of x is",x)
# # print("value of y is",y)
# """method 2"""
# # a = 39
# # b = 68
# # a,b = b,a
# # print(b)
# # print(a)
# #write a program to convert a float into integer.
# # x = 12.4
# # print(type(x))
# # x = int(x)
# # print(type(x))
# # print(x)
#  """write a progrsm to take details from a student for ID-CARD and then print in differnet lines"""
# # name = input("enter the name of student: ")
# # grade = input("enter the grade of the student: ")
# # age = int(input("enter the age of the student: "))
# # email = input("enter the email of the students: ")
# # ph_no = input("enter the phone number of the student: ")
# # print("Student Identity Card")
# # print(name)
# # print(grade)
# # print(age)
# # print(email)
# # print(ph_no)

# #write a program to take an user input as interger the convert it ionto float

# a = int(input("enter a number here: "))
# print (a)
# print (type(a))
# a = float(a)
# print ("after conversion",a)
# print(type(a))
#arithmetic operator
# print(8%3)#(modulus)
# print(13//3)#floor
# print(2**10)#exponen
#comparision
# print(6>10)
# print(3!=3)
# print(3>=3)
#logical
#print(not(3>4 and 3<4))
#identity
# a = 1234
# b = "1234"
# print(a is b)
# a  = 1234
# b = 1234
# print(a is not b)
#bitwise
# print(bin(151))
# print(10&8)
# print(10|8)
# print(10^8)
# print(10>>1)
# print(10<<2)
# #membership operator
# a = "helllo"
# print ("p" not in a)
#conditional statements
"""if statement"""
# marks = 55

# if marks >= 90:
#     print ("you will get a mobile phone")
    
# print ("thank you")

"""if else statement"""
# marks = 87

# if marks >= 90:
#     print ("you will get a phone")
# else:
#     print("no phone for a month")

# print("thank you")
# marks = 97

# if marks >= 90:
#     print ("you will get a phone")
# else:
#     print("no phone for a month")

# print("thank you")

"""if-elif-else statement"""
# marks = 50
# if marks >= 90:
#     print("you will go on trip")
# elif marks >= 80 and marks < 90:
#     print("you will get a new phone")
# elif marks >= 70 and marks < 80:
#    print("you will get a new book")
# else:
#     print("you will not get your phone back")
"""nested if statement"""
# marks = 96
# if marks >= 80:
#     print("you will get a new phone")
#     if marks >= 95:
#         print("you will go to a trip")
# else:
#     print("you will not get your phone for a month")
""""short hand if statement"""
# marks = 97
# if marks >= 90: print("you will get a new phone")
""""short hand if-else statement"""
# marks = 78
# print("you will get a new phone") if marks >= 90 else print("you will not get your phone for a month")


""""problem solving"""
#write a program to check if number is positive
# num = int(input("enter a number here: "))
# if num > 0:
#     print("it is positive")
# else:
#     print("it is not positive")
#write a program to check if number is even or odd
# num = int(input("enter a number here: "))
# if num % 2 == 0:
# 	print("it is even")
# else:
# 	print("it is odd")
# write a program to create a area calculator
# print("*****AREA CALCULATOR*****")
# print("""press 1 to get the area of square
# press 2 to get the area of rectangle
# press 3 to get the area of circle
# press 4 to get the area of triangle""")
# choice = int(input("enter a number bertween 1-4: "))
# if choice == 1:
#     side = float(input("enter the length of one side: "))
#     area = side**2
#     print("the area of square is",area)
# elif choice == 2:
#     length = float(input("enter the length of rectangle: "))
#     width = float(input("enter the width of rectangle: "))
#     area = length * width
#     print("the area of rectangle is",area)
# elif choice == 3:
#     radius = float(input("enter the radius of circle: "))
#     area = 3.14 * radius**2
#     print("the area of circle is",area)
# elif choice == 4:
#     base = float(input("enter the base of triangle: "))
#     height = float(input("enter the height of triangle: "))
#     area = 0.5 * base * height
#     print("the area of triangle is",area)
# else:
#     print("invalid choice")
# write a program check whether the passed letter is a vowel or not.
# letter = input("enter a letter here: ").lower()
# if letter in "aeiou":
#     print("it is vowel")
# else:
#     print("it is not a vowel")

    #WRITE A PROGRAM TO CHECK IF A NUMBER IS SINGLE DIGIT NUMBER , DOUBLE DIGIT NUMBER AND SO ON ....,UPTO 5 DIGIT NUMBER
    # num = int(input("enter a number here up to 5 digits: "))
    # if num >=0 and num <= 9:
    #     print("it is a single digit number")
    # elif num >= 10 and num <= 99:
    #     print("it is a double digit number")
    # elif num >= 100 and num <= 999:
    #     print("it is a triple digit number")
    # elif num >= 1000 and num <= 9999:
    #     print("it is a four digit number")
    # elif num >= 10000 and num <= 99999:
    #     print("it is a five digit number")
    # else:
    #     print("invalid input")

""" introduction to loops"""
# for loop
# for i in range(1, 6,2):
#     print(i)
#     print("hello world")  
# n = int(input("enter a number here: "))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)

# WHILE LOOP
# n = 0
# while n <= 50:
#     print (n)
#     n +=5
# n = 1
# a = int(input("enter a number here: "))
# while n <= 10:
#     print(a,"X",n,"=",a*n)
#     n +=1
#while true loop

# n = 1
# while True:
#     print("n")
#     n += 1

# while True:
#     num1 = int(input("enter a number here: "))
#     num2 = int(input("enter another number here: "))
#     print(num1 + num2)
#     repeat = input("do you want to continue? (yes/no): ").lower()
#     if repeat != "yes":
#         break

# nested loop
# for i in range(1, 4):
#     for j in range (1, 11):
#         print( j, end ="")
#         print ()

# for i in range(1, 10):
#     if i == 5:
#         print ("add this to the favs")
#     else:
#         print(i).
# for i in range(1, 101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)

# n = 1

# while n <= 10:
#     if n == 3:
#         print("add this to the favs")
#     else:
#         print(n)
#     n += 1
"""break and continue statement"""
# break statement: used to exit the loop completely
# continue statement: used to skip the current iteration and move to the next iteration
# for i in range (1, 11):
#     if i == 5:
#         continue
#     else:
#      print(i)
# for i in range(1, 11):
#     if i == 8:
#         break
#     else:
#         print(i)
"""problem solving"""
#write a program to find the sum of all the even numbers between 1 to 100
# sum = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         sum += i
#         print("the sum of all the even numbers between 1 to 100 is",sum)
#write a program to write first 20 numbers and their squared numbers.
# for i in range(1, 21):
#     print(i, "squared is", i**2)
#write a program to find the sum of first 10 odd numbers using while loop.
# sum = 0
# n = 0
# while n <= 20:
#     if n % 2 != 0:
#         sum += n
#     n += 1
# print("The sum of the first 10 odd numbers is:", sum)
#write a program to check if a number is divisible by 8 and 12 , up to 100 numbers.
# for i in range (1, 101):
#     if i % 8 == 0 and i % 12 == 0:
        #print(i)
        # write a program to create a billling system in supermarket.
# while True:
#     print("*****WELCOME TO SUPERMARKET*****")
#     name = input("enter your name here: ")
#     total = 0
#     while True:
#         print("enter the amount and quantity")
#         amount = float(input("enter the amount of item: "))
#         quantity = float(input("enter the quantity of item: "))
#         total += amount * quantity
#         repeat = input("do you want to add more items? (yes/no): ").lower()
#         if repeat == "no":
#             break

#     print("-" * 40)
#     print("Name:", name)
#     print("Amount to be paid:", total)
#     print("-" * 40)
#     print("thank you for shopping with us")
#     repeat = input("do you want to continue shopping? (yes/no): ").lower()
#     if repeat == "no":
#         break
"""problem solving"""
a= "Why fit in , when you are born to stand out" 
# #write a program to find the length of the following string.
# b = (len(a))
# print("the length of the string is",b)
# #write a program to check how many time alphabet o in occurs in the string.
# c = a.count("o")
# print("the number of times 'o' occurs in the string is",c)
# #write a program to convert the string into upper case and lower case.
# d = a.upper()
# print("the string in upper case is",d)
# e= a.lower()
# print("the string in lower case is",e)
# #write a program to convert the string into title. 
# f = a.title()
# print("the string in title case is",f)
#write a program to find the index number of "fit in" in the string.
# print(a.find("fit in"))
#pattern problem
# for i in range(1, 6):  # rows
#     for j in range(1, i + 1):  # columns
#         print("*", end="")
#     print()
# for i in range(1, 6):  # rows
#     for j in range(1, i + 1):  # columns
#         print(i, end="")
#     print()
# for i in range(1, 6):  # rows
#     for j in range(6,i,-1):  # columns
#         print(i, end="")
#     print()
# for i in range(1, 6):  # rows
#     for j in range(5,i,-1):  
#         print(" ", end=" ")
#     for k in range(i):  
#         print("*", end=" ")
#     print()
# # Upper Star Pattern
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# # Lower Star Pattern
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# for i in range (1,11):
#     for j in range(1, i+1):
#         print(i*j, end=" ")
#     print()

"""string manipulation"""
# #string is a cobination of numbers, alphabets and special characters, inclosed in single or double quotes.
# a = "Harry Potter and the goblet of fire"
# #to find the length of the string
# print(len(a))
# #to find the number of times a character occurs in the string
# print(a.count("o"))
# #to convert the string into upper case
# print(a.upper())
# #to convert the string into lower case
# print(a.lower())
# #to convert the string into title case
# print(a.title())
# #to find the index of a character in the string
# print(a.find("o"))
# #to convert the first letter to capital
# print(a.capitalize())
# #to convert a string into lower case
# print(a.casefold())
# #to find the index number of a character in the string
# print(a.index("o",15,34))
# #to write  variable inside a string
# name = "prince"
# age = 24
# b = f"my name is {name} and I am {age} years old"
# print(b)
# #it fill the given charaters and centralizes a string
# print(name.center(20,"*"))
"""string function"""
a = "hello"
b = "123hello"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.234"
h = "Harry Potter And The Goblet Of Fire"

# isalnum - Returns True if all characters in the string are alphanumeric
# print(a,a.isalnum())
# print(b,b.isalnum())
# print(c,c.isalnum())
# print(d,d.isalnum())
# print(e,e.isalnum())
# print(f,f.isalnum())
# print(g,g.isalnum())
# isalpha - Returns True if all characters in the string are in the alphabet
# print(a,a.isalnum())
# print(b,b.isalnum())
# print(c,c.isalnum())
# print(d,d.isalnum())
# print(e,e.isalnum())
# print(f,f.isalnum())
# print(g,g.isalnum())
# isdecimal - Returns True if all characters in the string are decimals
# print(a,a.isdecimal())
# print(b,b.isdecimal())
# print(c,c.isdecimal())
# print(d,d.isdecimal())
# print(e,e.isdecimal())
# print(f,f.isdecimal())
# print(g,g.isdecimal())
# isdigit - Returns True if all characters in the string are digits
# print(a,a.isdigit())
# print(b,b.isdigit())
# print(c,c.isdigit())
# print(d,d.isdigit())
# print(e,e.isdigit())
# print(f,f.isdigit())
# print(g,g.isdigit())
# isnumeric - Returns True if all characters in the string are numeric
# print(a,a.isnumeric())
# print(b,b.isnumeric())
# print(c,c.isnumeric())
# print(d,d.isnumeric())
# print(e,e.isnumeric())
# print(f,f.isnumeric())
# print(g,g.isnumeric())
# islower - Returns True if all characters in the string are lower case
# print(a,a.islower())
# print(b,b.islower())
# print(c,c.islower())
# print(d,d.islower())
# print(e,e.islower())
# print(f,f.islower())
# print(g,g.islower())
# isupper - Returns True if all characters in the string are upper case
# print(a,a.isupper())
# print(b,b.isupper())
# print(c,c.isupper())
# print(d,d.isupper())
# print(e,e.isupper())
# print(f,f.isupper())
# print(g,g.isupper())
# isspace - Returns True if all characters in the string are whitespaces
# print(a,a.isspace())
# print(b,b.isspace())
# print(c,c.isspace())
# print(d,d.isspace())
# print(e,e.isspace())
# print(f,f.isspace())
# print(g,g.isspace())
# istitle - Returns True if the string follows the rules of a title
# print(a,a.istitle())
# print(b,b.istitle())
# print(c,c.istitle())
# print(d,d.istitle())
# print(e,e.istitle())
# print(f,f.istitle())
# print(g,g.istitle())
# print(h,h.istitle())
# endswith() - Returns true if the strings ends with the specified value
# a = "Harry Potter"
# print(a.endswith("t"))
# startswith() - Returns true if the strings starta with the specified value
# a = "harry potter"
# print(a.startswith("h"))
# swapcase() - swaps case , lower case becomes upper case and vice versa
# a = "PRINCE UPADHYAY"
# print(a.swapcase())
# strip() - returns a trimmed version of the string
# a =  "  ******* prince upadhyay......."
# print(a.strip(".,*, "))
# split() - splits the string at the specified separator, and returns a list 
# a  = "#oofd#brb#omw#tb"
# b = "hello. my name is jhon. i am 23 years old"
# print(a.split("#"))
# print(b.split("."))
# ljust() - returns a lef justfied version of my string
# a =  " prince upadhyay"

# x = a.ljust(20,"*")

# print(x, " this is my name ")
# rjust() - returns a first justified version of the string
# a = "Prince Upadhyay"
# x = a.rjust(20,"*")
# print(x,"this is my name")
# replace() - retuns a string where a specified value is replaced with a specified value
# a =(("my name is liza"))
# print(a)
# print (a.replace("liza","pprince"))
# rindex() - searches the sttring for a specified value and returns the last position of where it was found
# a = "Harry Potter and the Prisoner of Azkaban"
# print(a.rindex("Prisoner"))
# rfind()
# a = "Harry Potter and the Prisoner of Azkaban"
# print(a.rfind("i"))
"""slicing in string"""
# a =  "Harry Potter and the Goblet of fire"
# b ="0123456789"
# print(a)
# print(a[0:5])
# print(a[6:12])
# print(a[:5])
# print(a[-4:])
# print(b[::6])
# print(b[:7:2])
# print(b[::-1])
# print(b[6::-1])
"""problem solving"""
#write a program to get fibonacci series up to 10 numbers
a = 0
b = 1
n = int(input("enter a number here : "))
if n == 1:
      print(1)
else:
      print(a)
print(b)
for i in range (2,n):
      c = a+b
      a = b
      b = c
      print(c)



