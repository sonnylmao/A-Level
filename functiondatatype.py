import random
import string
import datetime
nice = []

def randomtype():
  nice.append(random.randint(1,6969)) #INTEGER
  nice.append(random.uniform(1,6969)) #REAL
  nice.append(random.choice(string.ascii_letters))#CHAR
  nice.append("".join(random.choice(string.ascii_letters) for x in range(random.randint(10,30)))) #STRING
  nice.append(random.choice(["TRUE","FALSE"])) #BOOLEAN
  nice.append(datetime.date(random.randint(1900,2100),random.randint(1,12),random.randint(1,28))) #DATE
  print(*nice,sep="\n")
print(randomtype())
