#We wish to create a program to help the robot communicate with Beep.
print("Please enter a phrase?")
phrase = input()
bops = 0
while (bops < len(phrase)):
    print("Bop ", end="")
    bops = bops + 1