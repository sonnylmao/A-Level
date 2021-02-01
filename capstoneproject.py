import string
import random
import time
import math
from colorama import Fore, Back, Style

lives = 3
score = 0
c = 1

def empty(n):
    print("\n"*n)

def lines():
    print("===============================")

def correct():
    print(Fore.LIGHTGREEN_EX + "Correct!")
    score += 1
    print("score: ",score)
    time.sleep(1)

def wrong():
    print(Fore.RED + "wrong!")
    lives -= 1
    print("remaining lives: ",lives)
    time.sleep(1)
    
lines()
print(" welcome to the revision game!")
lines()
username = input("input your username: ")

time.sleep(1)
while lives != 0:
    empty(1)
    print(Style.RESET_ALL)
    print("round:", c)
    empty(1)
    ranstring = "".join(random.choice(string.ascii_letters) for x in range(random.randint(10,20)))
    #a = random.randint(1,3)
    a = 2
    
    #simple 
    if a == 1:
        b = random.randint(0,len(ranstring))
        print(ranstring+"[%s]" % str(b))
        userinp = input("what would this be?: ")
        if userinp == ranstring[b]:
            correct()
        else:
            wrong()

    #a bit more complicated, yikes!
    elif a == 2:
        b = random.randint(0,len(ranstring)-math.floor(len(ranstring)/2))
        c = random.randint(b,len(ranstring))
        print(ranstring+"[%s:%s]" % (str(b),str(c)))
        userinp = input("what would this be?: ")
        if userinp == ranstring[b:c]:
            correct()
        else:
            wrong()

    #super hard!!! omgg!!
    else:
        secondran = random.randint(0,1)
        b = random.randint(0,len(ranstring))
        if secondran == 0:
            print(ranstring+"[:%s]" % str(b))
            userinp = input("what would this be?: ")
            if userinp == ranstring[:b]:
                correct()
            else:
                wrong()
        else:
            print(ranstring+"[%s:]" % str(b))    
            userinp = input("what would this be?: ")
            if userinp == ranstring[b:]:
                correct()
            else:
                wrong()
    c += 1

print(Style.RESET_ALL)
print("Thank you for playing!")
print("Saving highscore...")

f = open("highscores.txt","a")
f.write(username,score)
f.close()