# -------------------------------------------
# CYOA GAME TEMPLATE - STUDENT VERSION
# Fill in all the >>> sections with your own story
# -------------------------------------------

print("The Legend of Momotarō (Peach Boy)")
print("Adapted from a flowchart")
player_name : str

# -------------------------------
# STARTING FUNCTION
# -------------------------------
def start():
    print("\n>>> Once upon a time, there was a boy")
    print(">>> This boby lived on an island in the middle of the ocean")

    choice = input(">>> Did this boy have a peach? (y / n): \n")

    if choice == "y":
        scene_A()
    elif choice == "n":
        scene_B()
    else:
        print("Invalid input. Try again.")
        start()


# -------------------------------
# SCENE A FUNCTION
# -------------------------------
def scene_A():
    print("\n>>> This boy was named Momotaro.")
    print(">>> Setting out for the ogres' island, he finds a dog")
    name = "Momotarō"

    choice = input(">>> Does the dog join him? (y / n): ")

    if choice == "y":
        ending_good()
    elif choice == "n":
        ending_bad()
    else:
        print("Invalid input.")
        scene_A()


# -------------------------------
# SCENE B FUNCTION
# -------------------------------
def scene_B():
    print("\n>>> Being a random homeless boy, he sets out on an adventure towards the ogres' island")


    player_name = input(">>> Choose a name to give him")

    print(">>> Finding a random dog on the way, he chooses for the dog to join him, since he has no friends.")
    
    scene_C()


# -------------------------------
# SCENE C FUNCTION
# -------------------------------
def scene_C():
    print("\n>>> On the way to the island, the dog starts barking")
    print(">>> Seemingly demanding for food, ")

    choice = input(">>> Does the boy divert to another island for food (y/n): ")

    if choice == "y":
        ending_neutral()
    elif choice == "n":
        ending_good()
    else:
        print("Invalid input.")
        scene_C()


# -------------------------------
# ENDINGS
# -------------------------------

def ending_good():
    print("\n>>> GOOD ENDING: With the help of the dog, you defeat the ogres")

def ending_bad():
    print("\n>>> BAD ENDING: You go to the island alone, and get immediately killed by an ogre's trap")

def ending_neutral():
    print("\n>>> NEUTRAL ENDING: You diverted for food, saving the adventure for another day")


# -------------------------------
# START GAME
# -------------------------------
start()
