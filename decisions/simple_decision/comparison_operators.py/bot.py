#we wish to compare number and give the response to the user if the number is greater than or smaller than the value entered 

First_number = int(input("Enter first number\n"))
Second_nnumber = int(input("Enter second number\n"))
if (First_number > Second_nnumber):
  print(First_number, "is bigger")
elif(First_number < Second_nnumber):
  print(First_number, "is smaller")
else:
  print("both numbers are equal")