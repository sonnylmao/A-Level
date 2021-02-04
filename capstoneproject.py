import string
import random
import datetime
import time
import math
from colorama import Fore, Back, Style #pip install colorama

lives = 3
score = 0
c = 1

def empty(n):
    print("\n"*n)

def lines():
    print("===============================")

def correct():
    print(Fore.LIGHTGREEN_EX + "correct!")

def wrong():
    print(Fore.RED + "wrong!")
    
lines()
print(" welcome to the revision game!")
lines()
username = input("input your username: ")

time.sleep(1)
while lives != 0:
    empty(1)
    print(Style.RESET_ALL)
    print("[ round:", c,"]")
    empty(1)
    ranstring = "".join(random.choice(string.ascii_letters) for x in range(random.randint(10,20)))
    a = random.randint(1,3)
    
    #easy round 
    if a == 1:
        b = random.randint(0,len(ranstring))
        print(ranstring+"[%s]" % str(b))
        userinp = input("what would this be?: ")
        if userinp == ranstring[b]:
            correct()
            score += 1
            print("score:",score)
            time.sleep(1)
        else:
            wrong()
            lives -= 1
            print("remaining lives:",lives)
            time.sleep(1)
    
    #a bit more complicated, yikes!
    elif a == 2:
        b = random.randint(0,len(ranstring)-math.floor(len(ranstring)/2))
        c = random.randint(b,len(ranstring))
        print(ranstring+"[%s:%s]" % (str(b),str(c)))
        userinp = input("what would this be?: ")
        if userinp == ranstring[b:c]:
            correct()
            score += 1
            print("score:",score)
            time.sleep(1)
        else:
            wrong()
            lives -= 1
            print("remaining lives: ",lives)
            time.sleep(1)

    #super hard!!! omgg!!
    else:
        secondran = random.randint(0,1)
        b = random.randint(0,len(ranstring))
        if secondran == 0:
            print(ranstring+"[:%s]" % str(b))
            userinp = input("what would this be?: ")
            if userinp == ranstring[:b]:
                correct()
                score += 1
                print("score:",score)
                time.sleep(1)
            else:
                wrong()
                lives -= 1
                print("remaining lives:",lives)
                time.sleep(1)
        else:
            print(ranstring+"[%s:]" % str(b))    
            userinp = input("what would this be?: ")
            if userinp == ranstring[b:]:
                correct()
                score += 1
                print("score:",score)
                time.sleep(1)
            else:
                wrong()
                lives -= 1
                print("remaining lives:",lives)
                time.sleep(1)
    c += 1

print(Style.RESET_ALL)
print("Thank you for playing!")
print("Saving highscore...")

f = open("highscores.txt","a")
f.write("\n %s \n" % datetime.datetime.now())
f.write("%s : %s " % (username, score))
f.close()
