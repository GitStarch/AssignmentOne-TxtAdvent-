

fightTypes = dict(Magic=0, Steel=0, Bow=0)
classMagic = {"Atk": 7, "Def": 3, "Spd": 6, "Strn": 5, "Health": 5}
classSteel = {"Atk": 5, "Def": 8, "Spd": 5, "Strn": 8, "Health": 5}
classBow = {"Atk": 3, "Def": 5, "Spd": 8, "Strn": 2, "Health": 5}
chosenClass = {} # Stores the players stats
inventory = {}
# Stores the information of each class (Fight Types).
while True:
    try:
        begin_PickFightType = str(input("What is your fighting type: Magic, Steel, Bow? ")).lower() # .lower allows the player the freedom to input "bow" with lower or upper case
        if begin_PickFightType == "magic":
            print("You are a Magi.")
            chosenClass = classMagic
            fightTypes["Magic"] = 1
            break
        if begin_PickFightType == "steel":
            print("You are one with might and metal.")
            chosenClass = classSteel
            fightTypes["Steel"] = 1
            break
        if begin_PickFightType == "bow":
            print("You traverse the world on an arrow.")
            chosenClass = classBow
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
print("It says: The Wooden House (Pointed North), The Cave (Pointed West), The Little Nifty Shop (Pointed East), and The Bookstore (Pointed North-West). ")
currentlocation = 0 #This will keep track of where the player is.

# WOODENSIGN will allow the player to go to different locations in the world depending on which direction they pick.

def woodensign():
    wsigndirection = {'north': 1, 'west': 2, 'east': 3, 'north-west': 4}
    global currentlocation
    direction = str(input("In which way would you like to go? ")).lower()
    if direction in wsigndirection:
        print("Okay, onward to the", direction) # end="." would have been used here but it was stopping me from continuing due to not allowing a newline.
        if direction == "north":
            currentlocation = 1
        if direction == "west":
            currentlocation = 2
        if direction == "east":
            currentlocation = 3
        if direction == "north-west":
            currentlocation = 4
    else:
        failed = str(input("Which way is that? North, West, East, or North-West? "))
        if failed in wsigndirection:
            print("Okay, onwards to the", failed) # end="." would have been used here but it was stopping me from continuing due to not allowing a newline.
            if failed == "north":
                currentlocation = 1
            if failed == "west":
                currentlocation = 2
            if failed == "east":
                currentlocation = 3
            if failed == "north-west":
                currentlocation = 4
# Depending on which direction the player picks, the game will give them different "gameplay" as they are going to different locations; currentlocation will be...
# ... updated and that variable will call on functions for whatever location the player is going to.

def thewoodenhouse():
    print("You begin moving North, up a stone pathway. Trees line the walkway and nature is blooming in this area of the world. After walking for an hour, and not seeing all too much, you come across a house.")
    print("You move closer to the innocuous building and realise you have a choice to make.")
    entry = input(str("Would you like to try to open the front door or go straight around the back? ")).lower()
    if entry == "open the front door" or entry == "front door":
        print("You creep up to the front door of the house, an old wooden door is the only thing between you and entry.")
        print("You knock. Once.... Twice.... Thrice.... No answer.")
        doorkick = str(input("Do you want to go round the back or attempt to kick the door in? ")).lower()
        if doorkick == "kick the door in" and chosenClass["Strn"] > 2: # The first skill check of the game, the code checks the "Strn" (Strength) stat of the player, if it is above 2 then they succeed.
           print("You kick the door through and it crashes to the floor with a bang. As you step inside you begin to see the wall decorations: shelves stacked with books, red and green rugs...")
           print("...and, surprisingly, no windows. The inside is dark, very dark, with an unlit candle atop an oak table in the middle of the room.")
           moveToCandle = str(input("Would you like to move closer to the candle or go over to one of the bookshelves? ")).lower()
           if moveToCandle == "move closer to the candle" or moveToCandle == "move closer":
               pickUpCandle = str(input("You move closer to the candle. It is stuck firmly to a brass stand. Do you pick it up? ")).lower()
               if pickUpCandle == "yes":
                   print("You pick up the candle.")
                   inventory["Candle"] = 1
                   print(inventory)
                   print("You make your way back out of the house, candle in pack, and go back to the sign.")
                   woodensign()
               else:
                   print("For some reason, you stare at the candle seemingly without intention.")
                   print("You leave the house, empty handed, and make your way back to the sign.")
                   woodensign()
           else:
               if moveToCandle == "go closer to the bookshelf" or moveToCandle == "go over to the bookshelf" or moveToCandle == "go over to one of the bookshelves" or moveToCandle == "go closer to the bookshelves":
                   print("You move closer to the bookshelves and begin looking at the book titles: 'Alden's Bright Future', 'The Forthcoming of Darkness', and 'Come Death, we Run'.")
                   whichBook = str(input("Which book would you like to look at? "))
                   if whichBook == "Alden's Bright Future":
                       print("You open up the old red book, blowing off the dust, and begin reading the first few pages. It details the journey of a long-dead warrior named Alden.")
                       print("Alden fought for many years, always for his people, and he always came out victorious. The scars he took home meant his life off the battlefield was one of pain.")
                       print("Unfortunately, Alden was forced to live with the pain and yet he carried on until passing away at an old age.")
                       print(chosenClass)
                       print("Your health raises by 2!")
                       chosenClass.update({"Health": 7})
                       print(chosenClass)
                       print("You place the book back onto the shelf and move out of the basement, back up the stairs and out of the house.")
                       print("Making your way back to the sign, you look back up to see where it points to next.")
                       woodensign()
                   if whichBook == "The Forthcoming of Darkness":
                       print("You pick up a black book, somehow free of dust. It tells the story of a brutal warrior, infamous for the cruelty and destruction he would cast upon battles.")
                       print("As you read, you feel something inside. Some kind of rage, some kind of apathy, some form barbarism.")
                       print(chosenClass)
                       print("Your attack raises by 2!")
                       if chosenClass == classMagic:
                           chosenClass.update({"Atk": 9})
                       if chosenClass == classSteel:
                           chosenClass.update({"Atk": 7})
                       if chosenClass == classBow:
                           chosenClass.update({"Atk": 5})
                       print(chosenClass)
                       print("You place the book back onto the shelf and move out of the basement, back up the stairs and out of the house.")
                       print("Making your way back to the sign, you look back up to see where it points to next.")
                       woodensign()
                   if whichBook == "Come Death, we Run":
                       print("You pick up a white book. The cover states 'Be Aware! Be Ready!'.")
                       print("Beginning to read the first page, the book talks about a creature that uses echo location to detect foes and evade them, outpacing death.")
                       print("The book details a scientific analysis of the creature, carried out by a J. F. Galdan.")
                       print(chosenClass)
                       print("Your speed raises by 2!")
                       if chosenClass == classMagic:
                           chosenClass.update({"Spd": 8})
                       if chosenClass == classSteel:
                           chosenClass.update({"Spd": 7})
                       if chosenClass == classBow:
                           chosenClass.update({"Spd": 10})
                       print(chosenClass)
                       print("You place the book back onto the shelf and move out of the basement, back up the stairs and out of the house.")
                       print("Making your way back to the sign, you look back up to see where it points to next.")
                       woodensign()
        else:
            print("You kick the door... BANG... you kick again... BANG.. OUCH! ...you cry out. You realise you've hurt your foot, not too much but enough to leave a mark.")
            print(chosenClass)
            chosenClass["Health"] = 4
            print(chosenClass)
            print("You lose 1 HP.")
    else:
        if entry == "go around the back" or entry == "around the back":
            print("You go around the side of the house. It looks old, with vegetation overtaking the outer side of the walls.")
            print("As you get to the back, you see the house has a backdoor. It is broken, rotted off it's hinges.")
            print("You easily push the door aside and move inside. It is dark with light leaking in from the broken door. You see a chest against the right wall and a stairway leading downstairs.")
            chestorNot = str(input("Do you want to take the stairs down or open up the chest? ")).lower()
            if chestorNot == "open the chest":
                print("You move over to the chest and check out the lock. Rotted, not dissimilar to the door. You give it a quick whack...")
                print("CLINK!")
                print("The lock falls to the ground and you open the chest.")
                inventory["Health Potion"] = 1
                print(inventory)
                print("You found a Health Potion!")
                print("You make your way back outside, back down the side pathway and to the sign.")
                woodensign()
            else:
                if chestorNot == "take the stairs down" or chestorNot == "take the stairs":
                    print("You move over to the top of the stairs and look down. It's dark, you can barely see the bottom.")
                    print("Taking your first step, they creek and seem to crack and splinter under your boot... SNAP!")
                    print("As you reach the middle of the stairs, they break and crumble beneath you. You tumble down and find yourself in a dark basement, devoid of light.")
                    print("You stand up and begin looking around, it's hard to see in the dark as you wait for your eyes to adjust. A scuttle can be heard a few steps away and so you move forward.")
                    print("As your eyes adjust more, you see a rat run into a hole. Looking up, you realise the hold is in a set of armour.")
                    takeArmour = str(input("Do you want to take the unbroken armour pieces? ")).lower()
                    if takeArmour == "yes":
                        print("You take the leggings, chestpiece, gauntlets and helmet.")
                        print(chosenClass)
                        print("Your defence raises by 2!")
                        if chosenClass == classMagic:
                            chosenClass.update({"Def": 5})
                        if chosenClass == classSteel:
                            chosenClass.update({"Def": 10})
                        if chosenClass == classBow:
                            chosenClass.update({"Def": 7})
                        print(chosenClass)
                        print("After putting on your new armour, you stretch a little and get comfortable in the metal.")
                        print("You go back up the stairs and out of the house, moving back to the sign and checking the other directions.")
                        woodensign()
                    else:
                        print("You decide that the hole in the armour is beneath you and leave it.")

def thebookstore():
    print("boooo")


woodensign()

if currentlocation == 1:
    thewoodenhouse()
if currentlocation == 2:
    thebookstore()
