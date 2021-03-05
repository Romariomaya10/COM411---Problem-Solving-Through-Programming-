print("what is your name?")
n = input() 
print("Do you have a dog? (types true or False)")
dog = input()
#bool is a boolean datatype - only stores True/False


if len(n) > 9 # allow lenth of exactly 9 or greater
 print("your have a very looong name!")
 print ("your name contains {} letters".format(len(n)))
elif len(n) > 6:
  print("Your name is a bitlong. Consider a nickname")
elif len(n) < 3:
  print("You name is quite ok")
print("This is the END of the program!")
