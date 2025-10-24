#imports
import time

#variables
hasStick:bool = False


#functions
def typeWrite(text:str, speed:int = 1):
    firstChar = True
    for letter in text:
        if letter == "\n" and not firstChar:
            time.sleep(1 * speed)
            print("")
            continue
        print(letter, end="")
        if letter == ",":
            time.sleep(0.5 * speed)
        else:
            time.sleep(0.02 * speed)
        
        firstChar = False
    print("")

def is_convertible_to_int(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def Response(question, *answers):
    constructedquestion:str = "\n" + question

    iteration = 1
    for i in answers:
        if i is None:
            continue
        
        constructedquestion += "\n" + str(iteration) + ": " + str(i)
        iteration += 1
    typeWrite(constructedquestion, 0.5)
    print("")
    response = input().lower()
    if is_convertible_to_int(response):
        if int(response) - 1 in range(len(answers)):
            return int(response)

    error:str = "Invalid input. Please enter 1"
    for i in range((len(answers) - 1)):
        error += " or " + str(i + 2)

    typeWrite(error + ".")
    time.sleep(0.5)
    return Response(question, *answers)

def startGame():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    typeWrite("Temple Walk, a Choose-Your-Own-Adventure game", 2)
    time.sleep(2)
    print("")
    typeWrite("You find yourself in a stone path.\nTwo illuminated torii shine bright-red in front of you.")
    time.sleep(1)
    typeWrite("Seeing the dimly-lit temple ahead, you proceed forward.\nAs you walk, you see a wooden stick to your right.")
    time.sleep(2)
    match Response("Take it with you?", "Yes, Hold it in your hand.", "Yes, Put it in your pocket.", "No, leave it be.", "No, throw it."):
        case 1:
            typeWrite("You picked up the stick. It has a green branch sticking out of it.")
            hasStick = True
        case 2:
            typeWrite("You picked up the stick and put it in your pocket. It is almost completely sticking out, but it stays put.")
            hasStick = True
        case 3:
            typeWrite("You ignored the stick")
        case 4:
            typeWrite("You threw the stick, it made a satisfying sound.")
            
    time.sleep(1)
    typeWrite("Continuing ahead, you reach the temple.")
    time.sleep(1.5)

#Ready
startGame()

#Feedback 
#I like the text animations and all of the branching paths but its not clear what the impact of the stick will be, gadiblud
#I dont really have much to say sincd its rlly short