import random

while 1:
 statement = input("What is your problem: ")

 if "help" in statement:
    therapy = random.randrange(1, 5)
    if therapy == 1:
        print("Nobody can help you")
    elif therapy == 2:
        print("I will not help you")
    elif therapy == 3:
        print("Are you weak? You need help?")
    elif therapy == 4:
        print("Help is just an excuse")
    elif therapy == 5:
        print("I need help, too. Will you help me?")
 elif "hello" in statement or "hey" in statement or "hi" in statement:
    therapy = random.randrange(1, 5)
    if therapy == 1:
        print("You can go away right away!")
    elif therapy == 2:
        print("Fuck off, nobody likes you")
    elif therapy == 3:
        print("Hey, just kiding, I dont like you!")
    elif therapy == 4:
        print("Hello and bye")
    elif therapy == 5:
        print("yeah, lets skip over the samll talk part")

 else:
  therapy = random.randrange(1, 10)
 
  if therapy == 1:
     print("Fuck you, idiot!")
  elif therapy == 2:
     print("Have you tried alcohol?")
  elif therapy == 3:
     print("Aha, I have the feeling you feel alone")
  elif therapy == 4:
     print("Mmmmh, I dont care")
  elif therapy == 5:
     print("Is this really the way you feel?")
  elif therapy == 6:
     print("I am the opinion you are insane")
  elif therapy == 7:
     print("This is the way!")
  elif therapy == 8:
     print("yah, no")
  elif therapy == 9:
     print("actually this is 100% true")
  else:
     print("Whatever, I cant help you!")

therapy = 0
statement = ""