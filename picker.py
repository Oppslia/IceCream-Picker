def openingStatement():
  print("\nType the number corresponding to your favorite ice cream\nIf you don't see your flavor listed, you can add one by typing 'add'\nType 'quit' when done \n")
flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Chocolate Chip Cookie Dough", "Cookies and Cream"]
counts = [0,0,0,0,0,0]
loopcount = 0 #stops loop




def flavorsList():
  increment = 1
  for flavor in range(len(flavors)):
      print(f'{increment}) {flavors[flavor]}')
      increment += 1

flavorsList()
openingStatement()

thisworks = 0 #increments value to iterate through a list in a for loop
while loopcount == 0:
  picks = input("What is your favorite listed ice cream flavor? ")
  if picks == "add":
    while True:
      newPick = input("Which flavor would you like to add?")
    
      if newPick.isdigit() == True:
        print("You eat number icecream??? try again")
        continue
        
      else:
        flavors.append(newPick)
        counts.append(0)
        flavorsList()
        break
    continue  
  if picks.lower() == "quit":
    loopcount = 1 #stops loop
    if sum(counts) == 0:
      print("No one likes icecream! D:")
      break
    for num in counts:
      personList = ["are", "people","enjoy"] # multiple people
      if num == 0:
        thisworks += 1 #this simple to remove 0's???? This variable keeps the lists parrallel, while not printing flavors that nobody picked.
      else:
        if num == 1:
          personList = ["is", "person","enjoys"] #single person
        print(f'There {personList[0]} {num} {personList[1]} who {personList[2]} {flavors[thisworks]}' )
        thisworks += 1  
      

  elif picks.isdigit() == False:
    print('Please enter a *number* corresponding to your flavor')
    continue
  elif picks == '0':
    print("0 doesn't correspond to a flavor")
    continue
  
  elif int(picks) in range(len(counts)+1):
    counts[int(picks) - 1] += 1 #takes position on list -1, then adds 1 to that position
    print(counts)
  else:
    print(f"{picks} doesn't correspond with a flavor")
