#he program should ask the user to enter three numbers (one number at a time) and should work out how many of these are even and odd. Finally, the program should display the number of even numbers and odd numbers entered.

First_number = int(input("Enter first number\n"))
Second_number = int(input("Enter second number\n"))
Third_number = int(input("Enter the Third number\n"))
First=First_number % 2
Second=Second_number % 2
Third=Third_number % 2
odd=0
even=0
if (First == 0):
  even+=1
else:
  odd+=1
if (Second == 0):
  even+=1
else:
  odd+=1
if (Third == 0):
  even+=1
else:
  odd+=1
print ("{} of those are odds, and {} are even numbers.".format(odd,even))

  
