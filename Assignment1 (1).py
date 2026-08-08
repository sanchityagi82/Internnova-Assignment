# Task 1
print("Welcome to Python Programming!")
name = input("Enter your Name: ")
college = input("Enter your College Name: ")
branch = input("Enter your Branch: ")
print("\n----- Student Details -----")
print("Name    :", name)
print("College :", college)
print("Branch  :", branch)

# Task 2 variables and datatypes
integer_value = 100
float_value = 98.5
string_value = "khushi"
boolean_value = True
print("Integer:", integer_value, "Type:", type(integer_value))
print("Float:", float_value, "Type:", type(float_value))
print("String:", string_value, "Type:", type(string_value))
print("Boolean:", boolean_value, "Type:", type(boolean_value))

# Task 3 operators
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("\nAddition:", num1 + num2)
print("\nSubtraction:", num1 - num2)
print("\nMultiplication:", num1 * num2)
if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
else:
    print("Division and Modulus cannot be performed because the second number is 0.")    

# Task 4 conditional statements
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# Task 5 Loops
# (a) print numbers from 1 to 20
for i in range(1,21):
    print(i)
#(b) Multiplication table
num = int(input("Enter a number:"))
for i in range(1,11):
    print(num, "x", i, "=", num*i)
#9(c) even numbers from 1 to 50 using while loop
i = 2 
while i <= 50:
    print(i)
    i = i + 2    

#Task 6 functions
def square(num):
    print("Square =", num * num)
def average(a, b, c):
    print("Average =", (a + b + c) / 3)
n = int(input("Enter a number: "))
square(n)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
average(x, y, z)   

#Task 7 Strings and collections
# String Operations
text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print(text.find("Programming"))

# List Operations
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
fruits.remove("Banana")
fruits.sort()
print(fruits)

# Tuple
t = (10, 20, 30, 40)
print(t)
print(t[1])

# Dictionary
student = {
    "Name": "Khushi",
    "Branch": "CSE",
    "College": "ABC College"
}
print(student)

# Set
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)

# Task 8 basic file handling
file = open("intro.txt", "w")
intro = input("Enter your introduction: ")
file.write(intro)
file.close()
file = open("intro.txt", "r")
print(file.read())
file.close()

# task 9 mini project
students = []
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        students.append({"Name": name, "Branch": branch})
    elif choice == "2":
        for s in students:
            print(s)
    elif choice == "3":
        name = input("Enter name to search: ")
        found = False
        for s in students:
            if s["Name"] == name:
                print(s)
                found = True
        if not found:
            print("Student not found")
    elif choice == "4":
        name = input("Enter name to delete: ")
        for s in students:
            if s["Name"] == name:
                students.remove(s)
                print("Record deleted")
                break
    elif choice == "5":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
