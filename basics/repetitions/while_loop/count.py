#We wish to create a program that allows Beep to avoid live cables.

print("How many live cables must I avoid?")
cable = int(input()) #user to enter the number of cables that beep will avoid
avoid = 1 #number 1 is to be added as it will be counting the cables 1 by 1
while (avoid <= cable ): #avoid cables is < or = to the number of cables
  print ("Avoiding...")
  print (f"...done! {avoid} live cable avoided!") #f for format to make sure the {avoid} will be display counting untill the final number entered by the user
  avoid = avoid + 1
print("All live cables have been avoided")
