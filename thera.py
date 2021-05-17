import random

while 1:
 statement = input("What is your problem: ")
 
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