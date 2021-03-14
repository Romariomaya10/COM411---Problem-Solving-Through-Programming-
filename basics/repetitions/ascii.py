# Ask user for number of bars for his phone battery

print("How many bars should be charged?")
bars_charging = int(input()) #bars that will be charged on the phone
bars_charged = 0
print() #the print will be depending of the input from the user
while (bars_charged < bars_charging):
    bars_charged = bars_charged + 1
    print("Charging:", "█ " * bars_charged)
    if (bars_charged < 5): #coonditionn based on bars charged loop
      print("not fully charged yet...")
if (bars_charged >= 5): # displayed if the input is higher than 5
  print("The battery is fully charged.") 