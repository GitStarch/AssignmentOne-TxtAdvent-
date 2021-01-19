fightTypes = dict(Magic=0, Steel=0, Bow=0)
# Stores the information of each class (Fight Types).
while True:
    try:
        begin_PickFightType = str(input("What is your fighting type: Magic, Steel, Bow? "))
        if begin_PickFightType == "Magic":
            print("You are a Magi.")
            fightTypes["Magic"] = 1
            break
        if begin_PickFightType == "Steel":
            print("You are one with might and metal.")
            fightTypes["Steel"] = 1
            break
        if begin_PickFightType == "Bow":
            print("You traverse the world on an arrow.")
            fightTypes["Bow"] = 1
            break
        # Each IF STATEMENT will assign the player the class they want, it will set the value (within the dict) of their class to 1 which will the make next IF STATEMENTS true.
    except KeyError:
        print("Please pick either the Magic, Steel, or Bow fighting types")
        break
    # finally:
    # print("Now we know your Fight Type, we can move on.")
    # break

if fightTypes["Magic"] == 1:
    print("As a Magi, you are a wielder of magic, using it to dampen and destroy your foes, and most past immovable objects.")
    fightTypes["Magic"] = 2
if fightTypes["Steel"] == 1:
    print("Being one with steel means you can bash through the hardest of walls and get up after the mightiest of hits!")
    fightTypes["Steel"] = 2
if fightTypes["Bow"] == 1:
    print("Having mastered the bow and arrow, you can take down foes with feathers from places they cannot even see.")
    fightTypes["Bow"] = 2
# Each IF STATEMENT will display a small piece of flavour text depending on the class you chose, confirming the class and letting the player know they have chosen the one they want.

print("Now your class has been chosen, we can begin our adventure.")
print("You, a Daylight Newborn, are emerging from a cave. Into bright sunlight, beaming onto green grass, you step out and see a wooden sign. ")
print("It says: The Wooden House (Pointed North), The Cave (Pointed West), The Little Nifty Shop (Pointed East), and The Bookstore (Pointed North-West) ")
currentlocation = 0

def woodensign():
    wsigndirection = {'North': 1, 'West': 2, 'East': 3, 'North-West': 4}
    currentlocation = 0
    failed = str
    direction = str(input("In which way would you like to go? "))
    if direction in wsigndirection:
        print("Okay, onward to the", direction, end=".")
    else:
        failed(input("Which way is that? North, West, East, or North-West? "))
        if failed in wsigndirection:
            print("Okay, onwards to the", direction, end=".")

woodensign()

#hhh
