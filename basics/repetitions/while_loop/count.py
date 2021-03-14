#We wish to create a program that allows Beep to avoid live cables.

print("How many live cables must I avoid?")
cable = int(input())
avoid = 1
while (avoid <= cable ):
  print ("Avoiding...")
  print (f"...done! {avoid} live cable avoided!")
  avoid = avoid + 1
print("All live cables have been avoided")
