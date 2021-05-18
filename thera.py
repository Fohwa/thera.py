import random
import pyttsx3 #for text to speech to make it more terrible

# the idea is to generate bools and categories. The bools score for the individual categories and the one with highest score will be chossen
# Alternative could be choosen to use lines with words missing, that will be added by another category, but this will be difficult

def speak(x):

   #initialise
   engine = pyttsx3.init()

   #sets a voice
   voices = engine.getProperty('voices') 
   engine.setProperty('voice', voices[1].id)

   #actual speaking
   engine.say(x)
   engine.runAndWait()


class category:
   linecount = 10

   line = ["Fuck you, idiot!", "Have you tried alcohol?",
   "Aha, I have the feeling you feel alone", "Mmmmh, I dont care",
   "Is this really the way you feel?", "I am the opinion you are insane",
   "This is the way!", "yeah, no", "actually this is 100% true",
   "Whatever, I cant help you!"]

normal = category()

while 1:
 statement = input("What is your problem: ")

 if "help" in statement:
    i = random.randrange(1, 5)
    help = category()
    help.line = ["Nobody can help you",
    "I will not help you", "Are you weak? You need help?",
    "Help is just an excuse", "I need help, too. Will you help me?", ]

    print(help.line[i])
    speak(help.line[i])

    
    
 elif "hello" in statement or "hey" in statement or "hi" in statement:

    i = random.randrange(1, 5)
    hi = category()
    hi.line = ["You can go away right away!", "Fuck off, nobody likes you",
    "Hey, just kiding, I dont like you!", "Hello and bye",
    "yeah, lets skip over the samll talk part", ]
    
    print(hi.line[i])
    speak(hi.line[i])

 else:
  i = random.randrange(1, 10)

  print(normal.line[i])
  speak(normal.line[i])


