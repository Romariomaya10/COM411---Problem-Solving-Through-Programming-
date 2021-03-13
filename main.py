#We wish to create a program that allows Beep to pick an adventure.
print("What type of adventure should I have?")
adventure = input() 
if ((adventure == "scary") or (adventure == "short")):
  print("Entering the dark forest!")
elif  ((adventure == "safe") or (adventure == "long")):
  print ("Taking the safe route!")
else:
  print("Not sure which route to take.")