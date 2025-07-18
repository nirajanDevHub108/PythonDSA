#---------------------Function Defination-------------------

#function for login authentication
def login():
  username = "nirajan"
  password = "password123"

  attempts = 3
  while attempts > 0:
    user= input("Enter your username :")
    pwd = input("Enter your password :")
    if user == username and pwd == password:
      print("Login successfully \n")
      return True
    else:
      print(f"Invalid credentials. {attempts} attempts left.\n")
      attempts -= 1

  print("Login failed. Maximum attempts reached.\n")
  return False



#function for add
def add(a , b):
  return a + b

#function for sub
def sub(a, b):
  return a - b

#function for mul
def mul(a , b):
  return a * b

#function for division
def div( a, b):
  if b != 0:
    return a / b
  else:
    return "Cannot divide by zero"

#main program loop
def calculator():
  print("welcome to python calculator !")

  while True:
    print( "\n select the operation :")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    choice = input("Enter you choice (1 - 5: ")

    if(choice == "5"):
      print("Exiting the Calculator . Good Bye !")
      break

    #input numbers
    try:
      num1 = float(input("Enter first number :"))
      num2 = float(input("Enter second number :"))
    except ValueError:
      print("Invalid input. Please enter valid numbers.")
      continue

    #perform operations
    if choice == "1":
      print("Result :",add(num1 , num2))
    elif choice == "2":
      print("Result :",sub(num1 , num2))
    elif choice == "3":
      print("Result :",mul(num1 , num2))
    elif choice == "4":
      print("Result :",div(num1 , num2))
    else:
      print("Invalid choice. Please select a valid operation (1 - 5).")
    
#running the calculator
if login():
  calculator()