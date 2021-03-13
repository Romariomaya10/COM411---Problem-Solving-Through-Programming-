#We wish to create a program that allows Beep to classify his books.

print ("What type of cover does the book have?")
Cover = input()
if (Cover == "Soft"): 
  print("Is the book perfect-bound?")
perfect_bound = input()
if (perfect_bound == "Yes"):
  print("Soft cover, perfect bound books are very popular!")
else:
  print("I am using Kindle instead  :P")
