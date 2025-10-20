#imports
import time

#variables
hasStick:bool = False


#functions
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
    
    response = input(constructedquestion + "\n").lower()
    if is_convertible_to_int(response):
        if int(response) - 1 in range(len(answers)):
            return int(response)

    error:str = "Invalid input. Please enter 1"
    for i in range((len(answers) - 1)):
        error += " or " + str(i + 2)

    print(error + ".")
    time.sleep(0.5)
    return Response(question, *answers)

def startGame():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Temple Walk, a Choose-Your-Own-Adventure game")
    time.sleep(2)
    print("\nYou find yourself in a stone path.\nTwo illuminated torii shine bright-red in front of you.")
    time.sleep(2)
    print("Seeing the dimly-lit temple ahead, you proceed forward.\nAs you walk, you see a wooden stick to your right.")
    time.sleep(2)
    match Response("Take it with you?", "Yes, Hold it in your hand.", "Yes, Put it in your pocket.", "No, leave it be.", "No, throw it."):
        case 1:
            print("You picked up the stick. It has a green branch sticking out of it.")
            hasStick = True
        case 2:
            print("You picked up the stick and put it in your pocket. It is almost completely sticking out, but it stays put.")
            hasStick = True
        case 3:
            print("You ignored the stick")
        case 4:
            print("You threw the stick, it made a satisfying sound.")
            
    time.sleep(2)
    print("Continuing ahead, you reach the temple.")
    time.sleep(1.5)

#Ready
startGame()

