#We wish to create a program that allows us to help Beep learn to paint. The program should start by prompting the user for a direction to move the paint brush (up, down, left or right). The program should then work out in which direction Beep should paint and display a suitable message.
print("Towards which direction should I paint?")
options = "up", "down", "left", "right"
options = input ()
if(options == "up"):
  print("I am painting in the upward direction!")
elif(options == "down"):
  print("I am painting in the downwards direction!")
elif(options == "left"):
  print("I am painting in the lef direction!")
elif(options == "right"):
  print("I am painting in the right direction!")
else:
  print ("not painting")