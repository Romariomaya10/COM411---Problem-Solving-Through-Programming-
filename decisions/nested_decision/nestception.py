#Beep is looking for his spare battery.


print("where should I look?")
look = input()
if (look == "In the bedroom"):
  print("Where in the bedroom should I look?")
  bedroom = input()
  if (bedroom == "Under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery") 
  bathroom = input()
  if (bathroom == "in the bathroom"):
    print("Where in the bathroom should I look?")
  bathtub = input()
  if (bathtub == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery")
  lab = input()
  if (lab == "in the lab"):
    print("Where in the lab should I look")
  table = input() 
  if (table == "on the table"):
    print ("Yes! I found my battery!")
  else:
    print ("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking")
