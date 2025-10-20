#imports
import time

#variables

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
    time.sleep(1)
    print("\nYou find yourself in a stone path.\nTwo illuminated torii shine bright-red in front of you.")
    time.sleep(1)
    match Response("What is your name?", "Jeff", "John", "Mr bean"):
        case 1:
            print("The killer guy?")
        case 2:
            print("I don't think that's your name")
        case 3:
            print("ok")

#Ready
startGame()

