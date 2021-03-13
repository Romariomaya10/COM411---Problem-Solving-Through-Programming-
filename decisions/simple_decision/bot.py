#The program should start by prompting the user to enter a whole number.The program should then work out if the number is even or odd.Finally, the program should display a suitable message to indicate if the number is even or odd.

Number = int(input("Please enter a whole number\n"))
remainder = Number % 2 
if (remainder == 0):
  print(Number, "is an even Number")
else:
  print(Number, "is an odd Number")