import random
import string
import datetime

INTlol = random.randint(1,100) #INTEGER
REALlol = random.uniform(1,100) #REAL
CHARlol = random.choice(string.ascii_letters) #CHAR
STRINGlol = "".join(random.choice(string.ascii_letters) for x in range(random.randint(10,30))) #STRING
BOOLEANlol = random.choice(["TRUE","FALSE"]) #BOOLEAN
DATElol = datetime.date(random.randint(1900,2100),random.randint(1,12),random.randint(1,28)) #DATE

datatypes = ["INT","REAL","CHAR","STRING","BOOLEAN","DATE"]
lmaoxd = [INTlol, REALlol, CHARlol, STRINGlol, BOOLEANlol, DATElol]
newlist = list(zip(datatypes,lmaoxd))
random.shuffle(newlist)
datatypes, lmaoxd = zip(*newlist)

lives = 3 
points = 0
print("========================================")
print("Welcome to our amazing game :D")
print("-> This game is cAsE sEnSiTiVe!")
print("-> Type in the correct data type for each output")
print("-> Datatypes: INT, REAL, CHAR, STRING, BOOLEAN, DATE")
print("========================================")

count = 0
while lives != 0:
    if count == 6:
        break
    for x in range(len(lmaoxd)):
        print("Question",x+1)
        print(lmaoxd[x])
        userinput = input("What datatype is this?: ")
        if userinput == datatypes [x]:
            print("\nCorrect! +1 Points")
            points += 1
        else:
            print("\nIncorrect! -1 Lives")
            lives -= 1
            print("Lives Remaining:",lives)
        print("========================================")
        count += 1

if lives == 0:
    print("Game Over! You Lose.")
else:
    print("Congratulations! You've won!")
    print("Points =",points)
print("========================================")
