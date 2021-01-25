import random

fightTypes = dict(Magic=0, Steel=0, Bow=0)
classMagic = {"Atk": 7, "Def": 3, "Spd": 6, "Strn": 5, "Health": 5}
classSteel = {"Atk": 5, "Def": 8, "Spd": 5, "Strn": 8, "Health": 5}
classBow = {"Atk": 3, "Def": 5, "Spd": 8, "Strn": 2, "Health": 5}
chosenClass = {} # Stores the players stats
inventory = {}
gold = 0
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
    wsigndirection = {'north': 1, 'west': 2}
    global currentlocation
    direction = str(input("In which way would you like to go? ")).lower()
    if direction in wsigndirection:
        print("Okay, onward to the", direction) # end="." would have been used here but it was stopping me from continuing due to not allowing a newline.
        if direction == "north":
            currentlocation = 1
        if direction == "west":
            currentlocation = 2
    else:
        failed = str(input("Which way is that? North, West, East, or North-West? "))
        if failed in wsigndirection:
            print("Okay, onwards to the", failed) # end="." would have been used here but it was stopping me from continuing due to not allowing a newline.
            if failed == "north":
                currentlocation = 1
            if failed == "west":
                currentlocation = 2
# Depending on which direction the player picks, the game will give them different "gameplay" as they are going to different locations; currentlocation will be...
# ... updated and that variable will call on functions for whatever location the player is going to.

gold = 0
def Gobdeath():
    print("The goblin falls to the ground")
    global gold
    gold = random.randrange(10, 101)
    print(gold)

def death():
    print("You feel a warmth in your clothing... You feel weak... you-")
    quit()

playerSPDwin = 0 # Determines whether the player attacks first.
goblinSPDwin = 0 # Determine whether the goblin attacks first.

def compareSPD(a, b): # a will always be the player's "Spd" stat and b the enemy's.
    global playerSPDwin
    global goblinSPDwin
    if a > b:
        playerSPDwin = 1
        return True
    if b > a:
        goblinSPDwin = 1
        return False
# The above function (compareSPD) compares the "Spd" stat of both the player (chosenClass) and the goblin (goblinStats) and allows the one with the higher stat to attack first.

def goblin(): # This function is the fight that takes place between the goblin and the player.
    print("A goblin attacks!")

    whatClass = [] # Used to know what class the player is during the fight
    if fightTypes["Magic"] == 2:
        whatClass.append("Magic")
    if fightTypes["Steel"] == 2:
        whatClass.append("Steel")
    if fightTypes["Bow"] == 2:
        whatClass.append("Bow")

    goblinStats = {"Atk": 2, "Health": 4, "Def": 5, "Spd": 6}
    compareSPD(chosenClass["Spd"], goblinStats["Spd"])

    while goblinStats["Health"] > 1: # Keeps track of player heath
        if playerSPDwin == 1:
            print("You go first")
        attack = str(input("Do you want to attack? ")).lower()
        if attack == "yes" and whatClass == ["Steel"]:
            print("You swing your sword!")
            ATKchance = random.randrange(10, 101, 10)
            if ATKchance > 50:
                goblinStats["Health"] -= 2
                print("You hit the goblin!")
            gobATKchance = random.randrange(10, 101, 10)
            if gobATKchance > 50:
                chosenClass["Health"] -= 1
        if attack == "yes" and whatClass == ["Bow"]:
            print("You draw your bow!")
            ATKchance = random.randrange(10, 101, 10)
            if ATKchance > 20:
                goblinStats["Health"] -= 1
                print("You hit the goblin!")
                print(goblinStats["Health"])
            gobATKchance = random.randrange(10, 101, 10)
            if gobATKchance > 50:
                chosenClass["Health"] -= 1
                print(chosenClass["Health"])
        if attack == "yes" and whatClass == ["Magic"]:
            print("You ready your spells!")
            ATKchance = random.randrange(10, 141, 10)
            if ATKchance > 100:
                goblinStats["Health"] -= 3
                print("You hit the goblin!")
            gobATKchance = random.randrange(10, 100, 10)
            if gobATKchance > 60:
                chosenClass["Health"] -= 1
                print("You got hit!")
                if chosenClass["Health"] == 0:
                    death()
        else:
            print("The goblin attacks first.")
            attack = str(input("Do you want to attack? ")).lower()
            if attack == "yes" and whatClass == ["Steel"]:
                print("You swing your sword!")
                ATKchance = random.randrange(10, 101, 10)
                if ATKchance > 50:
                    goblinStats["Health"] -= 2
                    print("You hit the goblin!")
                gobATKchance = random.randrange(10, 101, 10)
                if gobATKchance > 50:
                    chosenClass["Health"] -= 1
            if attack == "yes" and whatClass == ["Bow"]:
                print("You draw your bow!")
                ATKchance = random.randrange(10, 101, 10)
                if ATKchance > 20:
                    goblinStats["Health"] -= 1
                    print("You hit the goblin!")
                    print(goblinStats["Health"])
                gobATKchance = random.randrange(10, 101, 10)
                if gobATKchance > 50:
                    chosenClass["Health"] -= 1
                    print(chosenClass["Health"])
            if attack == "yes" and whatClass == ["Magic"]:
                print("You ready your spells!")
                ATKchance = random.randrange(10, 141, 10)
                if ATKchance > 100:
                    goblinStats["Health"] -= 3
                    print("You hit the goblin!")
                gobATKchance = random.randrange(10, 100, 10)
                if gobATKchance > 60:
                    chosenClass["Health"] -= 1
                    print("You got hit!")
                    if chosenClass["Health"] == 0:
                        death()
    else:
        Gobdeath()


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
            roundBack = str(input("Would you like to leave with some dignity left or go around the back? ")).lower()
            if roundBack == "go around the back":
                 print("You go around the side of the house. It looks old, with vegetation overtaking the outer side of the walls.")
                 print("As you get to the back, you see the house has a backdoor. It is broken, rotted off it's hinges.")
                 print("You easily push the door aside and move inside. It is dark with light leaking in from the broken door. You see a chest against the right wall and a stairway leading downstairs.")
                 altchestorNot = str(input("Do you want to take the stairs down or open up the chest? ")).lower()
                 if altchestorNot == "open up the chest" or altchestorNot == "open the chest":
                     print("You move over to the chest and check out the lock. Rotted, not dissimilar to the door. You give it a quick whack...")
                     print("CLINK!")
                     print("The lock falls to the ground and you open the chest.")
                     inventory["Health Potion"] = 1
                     print(inventory)
                     print("You found a Health Potion!")
                     print("You make your way back outside, back down the side pathway and to the sign.")
                     woodensign()
                 else:
                     if altchestorNot == "take the stairs down" or altchestorNot == "take the stairs":
                          print("You move over to the top of the stairs and look down. It's dark, you can barely see the bottom.")
                          print("Taking your first step, they creek and seem to crack and splinter under your boot... SNAP!")
                          print("As you reach the middle of the stairs, they break and crumble beneath you. You tumble down and find yourself in a dark basement, devoid of light.")
                          print("You stand up and begin looking around, it's hard to see in the dark as you wait for your eyes to adjust. A scuttle can be heard a few steps away and so you move forward.")
                          print("As your eyes adjust more, you see a rat run into a hole. Looking up, you realise the hold is in a set of armour.")
                          altTakearmour = str(input("Do you want to take the unbroken armour pieces? ")).lower()
                          if altTakearmour == "yes":
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
                if roundBack == "leave" or roundBack == "leave with dignity" or roundBack == "leave with some dignity":
                    print("After your humiliating stunt, you instantly turn around. Ashamed. Embarrassed.")
                    print("You go back to the sign and look for the next location, never wanting to see that house, or that door, again.")
                    woodensign()

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
                        print("You leave the dark room empty handed and head back out of the house. You move back to the signpost and take another look.")
                        woodensign()

whichFloorHoldOne = 0
whichFloorHoldTwo = 0
floorOneChecked = 0
floorTwoChecked = 0
bothfloorsChecked = 0

def whichfloorladder():
    global whichFloorHoldOne
    global whichFloorHoldTwo
    global bothfloorsChecked
    whichFloor = str(input("Which floor would you like to get off at? 1 or 2? "))
    if whichFloor == "1":
        whichFloorHoldOne = 1
        bothfloorsChecked += 1
        floorone()
    if whichFloor == "2":
        whichFloorHoldTwo = 1
        bothfloorsChecked += 1
        floortwo()

if floorOneChecked == "1" and whichFloorHoldOne == "1":
    print("You've already checked that floor.")
    whichfloorladder()
if floorTwoChecked == "1" and whichFloorHoldTwo == "1":
    print("You've already checked that floor.")
    whichfloorladder()
if bothfloorsChecked == "2":
    print("")

def floorone():
    global floorOneChecked
    print("You step off at the first floor, it's a golden room, totally golden. You begin to marvel at the magnificence of the room. In the middle lies a chest, one of silver and a golden lock.")
    print("You walk up to the chest and take a closer look at the lock.")
    FoneStrcheck = str(input("Do you want to open the chest? ")).lower()
    if FoneStrcheck == "yes" and chosenClass["Strn"] > 7:
        print("You open it up and take a look inside")
        print("Within lies a key. You take it and place it within your pack.")
        inventory["Key"] = 1
        print(inventory)
        print("Successful, you turn around and go back to the ladder with a smile.")
        floorOneChecked = 1
        whichfloorladder()
    if FoneStrcheck == "yes" and chosenClass["Strn"] < 7:
        print("You try to pry open the lock with your hands, but to no avail. The chest stays tightly shut.")
        print("Your Strn isn't high enough")
        print("You turn around, defeated, and go back to the ladder.")
        floorOneChecked = 1
        whichfloorladder()
    else:
        print("You decide to leave the chest and return to the ladder.")
        floorOneChecked = 1
        whichfloorladder()

def floortwo():
    print("You move higher up the ladder and step off at the second floor.")
    print("The room is dark.")
    lampyes = 0
    if "Lamp" in inventory:
        lampyes = 1
    lamp = str(input("Do you want to use your lamp? ")).lower()
    if lamp == "yes" and lampyes == "1":
        print("You illuminate the room with the lamp. Before you, a white room appears. The walls are lined with paintings.")
        print("Some small, some large. They each depict a changing landscape each with a unique creature.")
        print("You eye one and it depicts a creature that is small and yet fierce.")
        print("It inspires within you the determination to be better.")
        chosenClass.update({"Health": 10})
        chosenClass.update({"Strn": 10})
        chosenClass.update({"Atk": 10})
    if lamp == "yes" and lampyes == "0":
        print("You do not have a lamp.")
    if lamp == "no":
        print("You realise you won't be able to see without the lamp, and leave.")
        print("You make your way all the back to the sign.")
        woodensign()

def theniftylittlestore():
    print("You move westwards, into a thicket of of dark trees. A narrow pathway guides you through them, luckily the sun still lights your way.")
    print("As the density begins to diminish, you eventually see a clearing. Within the spot free of green and wood, you see a nifty little store.")
    print("As you move closer, a goblin-like creature falls down from a tree and draws his sword in a panic upon seeing you.")
    print("Fight!")
    goblin()
    print("You defeat the goblin and step over it's body. Looking up at the bookstore, you go ahead and knock on the door.")
    print("A old man in a light blue robe answers the door. He begins to speak: 'Hello. What do you seek at the store today?'")
    weapon = []
    if chosenClass == "Magic":
        weapon = "Spellbook"
    if chosenClass == "Steel":
        weapon = "Sword"
    if chosenClass == "Bow":
        weapon = "Bow & Arrowset"
    print("Your gold:", gold)
    didbuy = 0
    shop = int(input("1. A new weapon - 25g"
          "2. A lamp - 8g"
          "3. A new set of armour - 80g"))
    if shop == "1" and gold > 25:
        print("You give the man some gold and he gives you a new", weapon)
        print(chosenClass)
        print("Your atk increases!")
        chosenClass["Atk"] += 2
        print(chosenClass)
        gold -= 25
        print(gold)
        didbuy = 1
    if shop == "1" and gold < 25:
        print("You cannot afford this.")
        print(gold)

    if shop == "2" and gold > 8:
        print("The man hands over an old lamp for a small sum of gold")
        print("You place the lantern into your pack.")
        inventory["Lamp"] = 1
        print(inventory)
        gold -= 8
        print(gold)
        didbuy = 1
    if shop == "2" and gold < 8:
        print("You cannot afford this.")
        print(gold)

    if shop == "3" and gold > 80:
        print("You slip into the new set of armour for a hefty amount of gold. It fits well.")
        print(chosenClass)
        print("Your def increases!")
        chosenClass["Def"] += 4
        print(chosenClass)
        gold -= 80
        print(gold)
        didbuy = 1
    if shop == "3" and gold < 80:
        print("You cannot afford this.")

    if didbuy == 1:
        print("After purchasing something from the man, he lets you into the store to look around. Moving in, you see the walls stacked with many items, new and old.")
        print("A large wooden ladder is over on the left side of the store. The man smiles as he sees you looking and gestures for you to ascend it.")
        ladder = str(input("Do you want to ascend the ladder? ")).lower()
        if ladder == "yes" or ladder == "ascend the ladder":
            print("As you climb the ladder, you realise the store is more of a tower than it seems from the outside.")
            whichfloorladder()
    else:
        if shop == "nothing" and didbuy == 0:
            print("The man thanks you for looking and then closes the door")
            woodensign()



woodensign() # The woodensign function allows the player to go to different locations by holding a value within the currentlocation variable and then loading code (each location) based on that variable.

if currentlocation == 1:
    thewoodenhouse()
if currentlocation == 2:
    theniftylittlestore()
