# This was Sample Python script
# Basic Calculator:

# This function performs additiion

def add(a, b):
   return a + b
# This function performs subtraction

def subtract(a, b):
   return a - b

# This function performs multiplication

def multiply(a, b):
   return a * b

#This function performs division

def divide(a, b):
  return a / b

print("Hello, Happy To see you ~!! Select the arithmetic operation.")

print("+")

print("-")

print("*")

print("/")

#User input, Keyboard Input

choice = input("Hello good to see you , please enter operator to use:")

A = int(input("Please enter first number: "))

B = int(input("Please enter second number: "))

if choice == '+':

   print(A,"+",B,"=", add(A,B))

elif choice == '-':

   print(A,"-",B,"=", subtract(A,B))

elif choice == '*':

   print(A,"*",B,"=", multiply(A,B))

elif choice == '/':

   print(A,"/",B,"=", divide(A,B))

else:

  print("Invalid input")
