#Program that displays a menu and allows the user to either see a nice message, calculate areas of rectangle or triangle or displays a times table for a number

print("Please choose and option from the menu:\n1-Nicemessage|n2-Area oof a rectangle\n3-Area of triangle\n4-Times table")

option = int(input())

if option == 1:
  print("today will be a good day")
elif option == 2:
  print("Enter the lenght of the rectangle:")
  1 + int(input())
  print ("Enter the width of the rectangle")
  w = int(input())
  area = w*1     
  print("The area of this rectangle was {}".format(area))
elif option == 3:
  print ("Enter the base of the triangle:")
  base = float(input())
  print("Enter the height of the triangle")
  height = float(input())
  area = 0.5*height*height
  print("what number would you like to see times table for")

  n = int(input())
  for i in range(1,11,1):
    print("{}x{} = {}".format(n,i,*i))


