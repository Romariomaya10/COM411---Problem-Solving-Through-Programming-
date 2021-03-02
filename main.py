print("what is your name?")
n = input() 
print("Do you have a dog? (types true or False)")
dog = input()
#bool is a boolean datatype - only stores True/False


if len(n) > 9 and dog == "True":
 print("your have a very looong name!")
 print ("your name contains {} letters".format(len(n)))
else:
  print("You name is quite ok")
print("This is the END of the program!")
