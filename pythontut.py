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
# for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end= " " )
    print()
# for i in range(1, 10):
#     if i == 5:
#         print ("add this to the favs")
#     else:
#         print(i)




