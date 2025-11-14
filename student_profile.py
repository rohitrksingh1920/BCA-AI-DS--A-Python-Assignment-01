#Task-1: Setup & Introduction

# Name: Rohit
# Roll Number: 2501060098
# Course: BCA(SP AI & DS)
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: 14 November 2025

print("WELCOME TO THE STUDENT PROFILE CONSOLE APP")

#Task-2: Input & Variables

student_full_name = input("Enter your full name: ")
roll_number = input("Enter your roll number: ")
program = input("Enter your program (e.g., BCA): ")
university_name = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
hobby = input("Entre your hobby: ")

#Task-3: Operators Demonstration

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# print("--- Arithmetic Operators ---")
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)
print(num1, "%", num2, "=", num1 % num2)
print(num1, "**", num2, "=", num1 ** num2)
print(num1, "//", num2, "=", num1 // num2)

# print("--- Assignment Operators ---")
a = num1
a += 3
print("after a += 3:", a)
a -= 1
print("and after a -= 1:", a)
a *= 2
print("and after a *= 2:", a)
a /= 2
print("and after a /= 2:", a)
a %= 3
print("and after a %= 3:", a)

# print("--- Comparison Operators ---")
print(f"{num1} == {num2}:", num1 == num2)
print(f"{num1} < {num2}:", num1 < num2)
print(f"{num1} > {num2}:", num1 > num2)


# print("--- Logical Operators ---")
print("not equal:", not (num1 == num2))
print("any number is -ve:", num1 < 0 or num2 < 0)
print("both numbers are +ve:", num1 > 0 and num2 > 0)

# print("--- Identity Operators ---")
print("num1 is num2:", num1 is num2)
print("num1 is not num2:", num1 is not num2)

# print("--- Membership Operators ---")
list = [1, 2, 3, 4, 5]
print(f"{int(num1)} in list:", int(num1) in list)
print(f"{int(num2)} not in list:", int(num2) not in list)

# Task-4: Python Strings & Formatting
# String Concatenation
intro = "Hello, my name is " + student_full_name + " and I am a " + university_name + " student"
print(intro)

# f-strings
greeting = (f"Hello, {student_full_name}! Welcome to the {program} program")
print(greeting)

# Escape characters
print("Using escape characters:\n\t\"Learning python!\"\n")

# String methods
print("Title case: ", student_full_name.title())
print("Uppercase: ", student_full_name.upper())
print("Lowercase: ", student_full_name.lower())
print("Counting letters 'h': ", student_full_name.lower().count('h'))
print("Replacing spaces: ", student_full_name.replace(" ", "-"))

#Task-5: Final Output — Student Profile Card

print("----------------------------------------")
print("        STUDENT PROFILE SYSTEM")
print("----------------------------------------")
print("Name: ", student_full_name)
print("Roll No: ", roll_number)
print("Program: ", program)
print("University: ", university_name)
print("City: ", city)
print("Age: ", age)
print("Hobby: ",hobby)
print("----------------------------------------")
print("Welcome to Python Programming!")

# Task-6: Bonus Task

def save_profile(name, roll, course, uni, city, age, hobby):
    with open("student_profile.txt", "w") as file:
        file.write("----------------------------------------\n")
        file.write("        STUDENT PROFILE SYSTEM\n")
        file.write("----------------------------------------\n")
        file.write("Name:      " + name + "\n")
        file.write("Roll No:   " + roll + "\n")
        file.write("Course:    " + course + "\n")
        file.write("University:" + uni + "\n")
        file.write("City:      " + city + "\n")
        file.write("Age:       " + str(age) + "\n")
        file.write("Hobby:     " + hobby + "\n")
        file.write("----------------------------------------\n")
        file.write("Welcome to Python Programming!\n")
    print("Profile saved successfully in 'student_profile.txt'.")


# Asking user choice
save = input("Do you want to save your profile? (yes/no): ")

if save == "yes":
    save_profile(student_full_name, roll_number, program, university_name, city, age, hobby)
else:
    print("Profile not saved. Thank you for using the app!")
