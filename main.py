print('--------------Covid or Nah-------------')

name = input("What is your name? ")
print("Welcome to LAC+USC Medical Center," + name + "! Determine if you have Covid or Nah")

total = 0
print("\n")
print("---How many of these symptoms do you have---")
print("  Do you have fever or chills? \n  Do you cough? \n   Do you have shortness of Breath? \n   Do you have body aches? \n   Do you have loss of taste or smell? \n   Do you have a runny nose? ")
total = int(input("How many do you have? "))
print("\n")

print("Please answer yes/no")
if total == 0:
  a = input("Have you traveled or have been exposed in the last 14days? ")
  if a == 'yes':
    c = input("Did you do all of this? Not wearing a mask touching of your face, touching of surfaces outside your home, and not socially distancing? ")
    if c == 'yes':
      print("Hey " + name + "! You need to get a Covid test!")
    else: 
      print("Hey " + name + "! You do not need to take a Covid test, but you need to keep track of the symptoms and if they begin to worsen, do not hesitate to get medical attention.!")
  else:
    print("Hey " + name + "! You do not need to get a Covid test!")
elif total == 1:
  b = input("Do you work at a healthcare? ")
  if b == 'yes':
    print("Hey " + name + "! You need to get a Covid test!")
  else:
    print("Hey " + name + "! You do not need to take a Covid test, but you need to keep track of the symptoms and if they begin to worsen, do not hesitate to get medical attention.!")
else:
  print("Hey " + name + "! You need to get a Covid test!")
