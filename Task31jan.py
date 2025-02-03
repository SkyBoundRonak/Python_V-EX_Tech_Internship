#Task 1: Write a program that takes name, age, and salary as input and prints them in a formatted string.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
print(f"Name: {name}, Age: {age}, Salary: {salary}")

#Task 2: Write a program that takes two numbers and performs addition, subtraction, multiplication, division, and modulus operations.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")

#Task 3: Write a Python program to check if a number is positive, negative, or zero.
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
#Task 4: Write a program to print the first 10 even numbers using both for and while loops.
# Using for loop
print("Using for loop:")
for i in range(2, 21, 2):
    print(i)

# Using while loop
print("Using while loop:")
count = 2
while count <= 20:
    print(count)
    count += 2
    
#Task 5: Create a tuple of fruits and convert it into a set.
fruits_tuple = ('apple', 'banana', 'cherry', 'apple', 'banana')
fruits_set = set(fruits_tuple)

print("Tuple:", fruits_tuple)
print("Set:", fruits_set)

#Task 6: Write a program to store student names and their marks in a dictionary, then print all students scoring more than 80.
students = {
    "Alice": 85,
    "Bob": 75,
    "Charlie": 90,
    "David": 80,
    "Eve": 95
}

print("Students scoring more than 80:")
for name, marks in students.items():
    if marks > 80:
        print(f"{name}: {marks}")

#Task 7:Write a Python program to read a file and count the number of lines.
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")

#Task 8: Write a program to handle division by zero error.
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")
    
#Task 9: Validate an email using regex.
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

email = input("Enter an email address: ")
if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")

#Task 10: Import the math module and use sqrt() function.
import math

number = float(input("Enter a number: "))
print(f"Square root of {number} is {math.sqrt(number)}")

#Task 11: Convert a Python dictionary to a JSON string and save it to a file.
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data, indent=4)
with open('data.json', 'w') as file:
    file.write(json_string)

print("JSON data saved to 'data.json'")

#Task 12: Send an email using Python.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configurating
sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
password = "your_password"

# Creating the email
subject = "Test Email"
body = "This is a test email sent from Python."

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Sending the email
try:
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")