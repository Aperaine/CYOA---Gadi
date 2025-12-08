#imports
import time

#variables
hasStick:bool = False
endings:int = 5

logo:str = """
 █                                                                              ████                
███████████████████████████████                                                 ████                
 ██████████████████████████████                                                 ████                
            ███                                                                  ███                
            ███            ████████                ██                            ████               
            ████         ████████████     ███   ███████                          ████    ████████   
            ████        █████     █████   ████ ████████                          ████  ████████████ 
            ████       █████████████████  ████████ ██████████          ██████     ███ ████    █████ 
            ████       █████████████████  ███████   ██████████   ██████████████   ███ ████████████  
             ████     ████                ██████    █████  ████  ██████     ████  ███ █████████     
             ████      ███                █████     █████   ████  ████       ████ ████ ████         
              ███      ████               █████      ████   ████  ████       ████  ███  ████        
              ████      █████             █████      ████    ████ ████       ███   ███   ██████     
               ███       █████        ███ ████       ████    ████ █████     ████   ███     █████████
               ███         ███████  █████ ████       ████     ██  ███████  ████    ████       ██████
                             ███████████    █         ██          ████████████     ████             
                                  ███                             █████ ████        ██              
                                                                  █████                             
                                                                   ████                             
      ██              █                                            ████                             
      ███           █████                            ██            ████                             
      ███          ██████                           ████           ████                             
      ███         ███████       ██                  ████  ████     ████                             
      ███        ████████     █████    ██           ████  ████      ███                             
      ███       ████ ████    ████   ███████         ████  ████      ███                             
      ████     ████  ████  █████  ██████████        ████  ████                                      
      ████    ████   ████ ████   ████  ██████       ████  ████                                      
       ████  ████    ████████   ████  █████████     ████  ████   █████                              
        ████████     ███████   ████ █████   █████   ████  ████ ██████                               
          █████       ████      ███████       █████ ████  ██████████                                
           ███                   ███            ███ ████  ████████                                  
                                                     ███   █████████                                
                                                           ███  ██████                              
                                                            █      ███                              
"""

#functions
def typeWrite(text:str, speed:float = 0.8):
    firstChar = True
    for letter in text:
        if letter == "\n" and not firstChar:
            time.sleep(1 * speed)
            print("")
            continue
        print(letter, end="")
        if letter == "," or letter == ".":
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
    typeWrite(constructedquestion, 0.75)
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

def Ending(text:str, num:int):
    typeWrite(text)
    time.sleep(1)
    typeWrite("Ending " + str(num) + " out of " + str(endings))
    input("Type anything to restart")
    startGame()

def startGame():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(logo)
    typeWrite("Temple Walk, a Choose-Your-Own-Adventure game", 2)
    time.sleep(2)
    print("")
    typeWrite("In the dark of the mindnight, You find yourself in a stone path.\nTwo illuminated torii shine bright-red in front of you.")
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
    typeWrite("You entered the temple grounds\nBright lanterns line the path\nThe mossy rocks provide a strange sense of comfort")
    time.sleep(1)
    match Response("Go inside?", "Enter the main tower", "Leave"):
        case 1:
            typeWrite("You entered the tower\nThere are some shiny props and statues behind a closed net.\nIn front of you, there's a little donation box")
            time.sleep(1)
            match Response("Donate 10 yen?","Donate","Don't donate"):
                case 1:
                    Donated()
                case 2:
                    NotDonated()
                    
        case 2:
            Ending("You left", 1)
            return()

def Donated():
    typeWrite("You drop 10 yen into the box.\nIt makes a loud *thunk* sound.\nYou can't see much, but the golden objects in the back appear to shine a little brighter")
    time.sleep(1)
    match Response("Leave?", "Leave the tower", "Wait"):
        case 1:
            pass

        case 2:
            typeWrite("You waited\nNothing happened")
            if Response("","Leave the tower","Wait") == 2:
                typeWrite("You waited\nStill, nothing happened")
                if Response("","Leave the tower","Wait") == 2:
                    typeWrite("You waited\nNothing is happening, you feel disappointed")
                    if Response("","Leave the tower","Wait") == 2:
                        typeWrite("You waited\nYou should probably leave the tower")
                        if Response("","Leave the tower","Wait") == 2:
                            typeWrite("You waited\n...")
                            if Response("","Leave the tower","Wait") == 2:
                                typeWrite("You waited\n...")
                                if Response("","Leave the tower","Wait") == 2:
                                    typeWrite("You waited\n...")
                                    if Response("","Leave the tower","Wait") == 2:
                                        typeWrite("You waited\nPlease leave")
                                        Response("","Leave the tower")
            
    typeWrite("You left the tower\nThe light of the glowing lanterns feels warm to your skin\nThe shadow of the tower feels alive\nYou are filled with determination")
    time.sleep(1)
    typeWrite("To the side, two paths emerge\nOne side reveals a narrow walkway\nThe other side shows a big shōrō")
    time.sleep(1)

    match Response("Where do you go?", "Walk the walkway", "Go to the bell"):
        case 1:
            StatueArea(True)

        case 2:
            Shoro(True)
    

def NotDonated():
    typeWrite("You didn't donate.")
    time.sleep(1)
    match Response("Leave?", "Leave the tower", "Wait"):
        case 1:
            pass

        case 2:
            typeWrite("You waited\n...But nobody came")
            Response("","Leave the tower")
            
    typeWrite("You left the tower\nThe wind feels awfully cold\nThe shadow of the tower appears to grow\n\n[[DETERMINATION]]")
    time.sleep(1)
    typeWrite("To the side, two paths emerge\nOne side reveals a narrow walkway\nThe other side shows a big shōrō")
    time.sleep(1)

    match Response("Which way?", "Walk the walkway", "Go to the bell"):
        case 1:
            StatueArea(False)

        case 2:
            Shoro(False)

def StatueArea(donated:bool):
    if donated: #donated route
        typeWrite("You walk through the ruined path.\nThe ground is covered in moss.\nHundreds of stone Jizo statues surround you\nThey wear uniquely fitted red beanies and bibs")
        time.sleep(1)
        typeWrite("At the end of the route, you find a monk praying to a statue\nYou can't tell what he's saying, or what his goal is at a time like this.")
        time.sleep(1)
        if Response("Approach him?", "Yes, keep going", "No, go towards the belltower instead") == 2:
            Shoro(True)
            return
        
        typeWrite("In an instant, he snaps his head back at you.")
        time.sleep(1)
        match Response('"Did you donate?"',"Yes","No"): #This isn't actualy for checking if the player donated, it's just extra dialogue
            case 1:
                typeWrite("\"That's what I thought...\"")
            case 2:
                typeWrite("\"You know, I can tell when people are lying\"")

        time.sleep(1)
        typeWrite("He looks amused\n\"This temple has been abandoned for decades. You are the first to come here since it shut down.\"")
        time.sleep(1)
        typeWrite("""He continues, "The spirits here require funds every so often to keep the place usable.
                  They're running out, and so that hundred yen you dropped could be enough to keep them going another year." """)
        time.sleep(1)
        typeWrite("\"If you're done exploring, it's very late. Go home.\"")
        if hasStick:
            time.sleep(1)
            typeWrite("He pauses for a second, \"Oh, and would you mind giving back that stick? It was a gift from a stray cat.\"")
            match Response("Give the stick back?", "Yes, Give it back", "No, keep it"):
                case 1:
                    typeWrite("You gave the stick back")
                case 2:
                    typeWrite("You kept the stick.\n\"...I'll just find another stick\"")
            
        time.sleep(1)
        typeWrite("\"Please come back if you ever pass by this place.\"")
        Ending("The monk is pleased with you.", 2)
    
    else: #genocide (not donated) route
        typeWrite("You walk through the ruined path.\nThe ground is covered in moss.\nHundreds of stone Jizo statues surround you\nThey wear uniquely fitted red beanies and bibs")
        time.sleep(1)
        typeWrite("At the end of the route, you find what appears to be a monk praying to a statue\nYou can't tell what he's doing, but he doesn't seem happy.")
        time.sleep(1)
        if Response("Approach him?", "Yes, keep going", "No, go towards the belltower instead") == 2:
            typeWrite("You think about turning around, but something tells you to keep going.")
            time.sleep(1)

        typeWrite("In an instant, he snaps his head back at you.")
        time.sleep(1)
        Response('"Why didn\'t you donate?", he asks somoberly',"1","2") #This isn't actualy for checking if the player donated, it's just extra dialogue
        time.sleep(1)
        typeWrite("He looks down\n\"This temple has been abandoned for decades. You are the first to come here since it shut down.\"")
        time.sleep(1)
        typeWrite("""He continues, "The spirits here require funds every so often to keep the place usable.
                  They're running out, and so they're gonna need another way to get what they need." """)
        time.sleep(1)
        typeWrite(""""If you had just donated, I wouldn't have had to do what I'm about to do.
Without funds, they're gonna need something more valuable.
Your soul, for instance, is something that they would crave."

He looks at you with a grim expression.
He chants a dialect you don't recognize.
You feel lighter that air, yet stuck to the ground.""")
        time.sleep(1)
        typeWrite("""Holding onto the 100 yen coin in your pocket, you stand still.
As you feel your feet turning hard, you think reconsider why you didn't donate""")
        if hasStick:
            time.sleep(1)
            typeWrite("Even the stick you took starts to harden")
        
        Ending("You turned to stone",4)


def Shoro(donated:bool): #shōrō is the japanese bell building
    if donated: #donated route
        typeWrite("""You walk towards the bell tower.
Under a bronze roof, a massive bell hangs overhead.
Before the bell, you see a cylindrical hammer with a rope danglling in front of you, waiting to be thrown""")
        match Response("Ring the bell?", "Ring it", "Don't ring it"):
            case 2:
                typeWrite("You chose not to ring the bell.\nThere isn't much else to do here.")
                match Response("Go somewhere else?", "Walk towards path", "Ring the bell"):
                    case 1:
                        StatueArea(True)
                        return
        
        typeWrite("""You pulled back the mallet, and threw it with as much force as you could muster.
The bell tolled with a booming ring.

In front of you, a yokai arises.
Its features are larger than of any human.
The yellow kimono appears looser than it should be.
Its mouth drools of devilish intent.""")
        time.sleep(1)
        typeWrite('''"You should be afraid," it murmurs
"At a time like this, statistics show that spiritual posessions are at an all time high...
Despite what that foolish monk says, there is no saving this sanctum at this point." He tells you

Taking a moment to think, it comes to a realization:
"Were you the one who donated that coin?" it asks''')
        time.sleep(1)
        Response("What do you say?", "Yes", "Yeah, but it was only 100 yen")
        typeWrite('''"Like I was saying, this temple is dead
The funds you provided are only enough for 132 spirits.
Others may not know this, but with the cemetary nearby, there are definetely not enough resources for all of us."

Thinking even harder, he comes up with an idea.
"We don\'t have what it takes to get that money... but what if we did?"''')
        
        match Response('"Would you be willing to sacrifice your body for the survival of this beacon?', "Yes", "No"):
            case 1:
                typeWrite('''You nod your head
"Great! Now we just need to see if you qualify.
Functional body - Check
10 Fingers - Check
Soullessness... uhh weren't you the one who donated the coin?"

You nod your head.
"Yeah, unfortunately you don't qualify.''')
            case 2:
                typeWrite("You shake your head")
        
        time.sleep(1)
        typeWrite("""Well in that case, we're screwed anyways.
Go back out where you came in, the exit's on your left""")
        time.sleep(1)
        Ending("You left the temple with a feeling of discomfort",3)
        

    else: #genocide (not donated) route
        typeWrite("""You walk towards the bell tower.
Under a bronze roof, a massive bell hangs overhead.
Before the bell, you see a cylindrical hammer with a rope danglling in front of you.""")
        match Response("Ring the bell?", "Ring it", "Don't ring it"):
            case 2:
                typeWrite("You thought of not ringing the bell, but something tells you that you should ring it anyway.")
        
        typeWrite("""You pulled back the mallet, and threw it with as much force as you could muster.
The bell tolled with a booming ring.

In front of you, a yokai arises.
Its features are larger than of any human.
The yellow kimono appears looser than it should be.
Its mouth drools of devilish intent.""")
        time.sleep(1)
        typeWrite('''"You should be afraid," it murmurs
"At a time like this, statistics show that spiritual posessions are at an all time high...
Despite what that foolish monk says, there is no saving this sanctum at this point." He tells you''')
        time.sleep(1)
        typeWrite('''"Like I was saying, this temple is dead
With the fact you came in here without even donating, you've upset a few ghosts." He notifies you.
Thinking even harder, he comes up with an idea.
"We don\'t have what it takes to get that money... but what if we did?"''')
        
        match Response('"Would you be willing to sacrifice your body for the survival of this beacon?', "Yes", "No"):
            case 2:
                typeWrite("Something is stoopping you from saying no")
                Response('"Well what\'s it gonna be? Posession or no possession?', "Yes")
        
        typeWrite('''You nod your head
"Great! Now we just need to see if you qualify.
Functional body - Check
10 Fingers - Check
Soullessness - Check"
It looks at you with a grin

"Well, posession time!"''')
        
        time.sleep(1)
        typeWrite("""You feel hyperaware as it takes over you with a swift motion
Losing consciousness, you're glad you never donated.""")
        time.sleep(1)
        Ending("You got posessed",5)


#Ready
startGame()

#Feedback 1
#I like the text animations and all of the branching paths but its not clear what the impact of the stick will be, gadiblud
#I dont really have much to say sincd its rlly short