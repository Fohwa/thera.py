import random
import pyttsx3 #for text to speech to make it more terrible
from playsound import playsound

# the idea is to generate bools and categories. The bools score for the individual categories and the one with highest score will be chossen
# Alternative could be choosen to use lines with words missing, that will be added by another category, but this will be difficult


def speak(x): #herlper function to speak a string

   #initialise
   engine = pyttsx3.init()

   #sets a voice
   voices = engine.getProperty('voices') 
   engine.setProperty('voice', voices[1].id)

   #actual speaking
   engine.say(x)
   engine.runAndWait()

#introduction
print("Hello, I am your personal therapist, because you cannot afford a real therapist. Lets begin!")
speak("Hello, I am your personal therapist, because you cannot afford a real therapist. Lets begin! So now tell me what the fuck is wrong with you")

class category: # layout for keywords
   linecount = 10

   line = ["Fuck you, idiot!", "Have you tried alcohol?",
   "Aha, I have the feeling you feel alone", "Mmmmh, I dont care",
   "Is this really the way you feel?", "I am the opinion you are insane",
   "This is the way!", "yeah, no", "actually this is 100% true",
   "Whatever, I cant help you!", "Please, just let me alone!",
   "I really dont want to see your ugly face", "you are worthless"]

normal = category()

while 1:
 statement = input("What is your problem: ")

 if statement == "stop":
    break

 elif "comrade" in statement: #meme for the comrades
    
    print("Sovetskoye tsarstvo vosstanet yeshche raz. Tak chto vse nashi lyudi mogut zhit' pod krasnym solntsem, tovarishch\n")
    speak("Sovetskoye tsarstvo vosstanet communisme yeshche raz. Putin Tak chto vse nashi vodga lyudi mogut zhit' Gorbatschof pod krasnym solntsem, comrade")
    
    #play sound
    playsound("D:/folder/sound/comrade.mp3")

 elif "hello world" in statement:
    
    print("Fuck off you fucking nerd\n")
    speak("Fuck off you fucking nerd")

 elif "help" in statement:
    i = random.randrange(1, 5)
    help = category()
    help.line = ["Nobody can help you",
    "I will not help you", "Are you weak? You need help?",
    "Help is just an excuse", "I need help, too. Will you help me?", ]

    print(help.line[i] + "\n")
    speak(help.line[i])

    
    
 elif "hello" in statement or "hey" in statement or "hi" in statement:

    i = random.randrange(1, 5)
    hi = category()
    hi.line = ["You can go away right away!", "Fuck off, nobody likes you",
    "Hey, just kiding, I dont like you!", "Hello and bye",
    "yeah, lets skip over the small talk part", ]
    
    print(hi.line[i] + "\n")
    speak(hi.line[i])

 elif "?" in statement:
    
    print("This is a stupid question\n")
    speak("This is a stupid question")


 else:
  i = int(random.uniform(1, 10))

  print(normal.line[i] + "\n")
  speak(normal.line[i])


