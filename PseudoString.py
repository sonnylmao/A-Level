def LEFT(string,length):
    return string[0:length]

def RIGHT(string,length): 
    return string[-length:]

def MID(string,start,end): 
    return string[start-1:end]
    
def LENGTH(string): 
    return len(string)

def LCASE(string): 
    return string.lower()
    
def UCASE(string): 
    return string.upper()

def TO_UPPER(string):
    return string.upper()
 
def TO_LOWER(string):
    return string.lower()
 
def NUM_TO_STRING(number):
    return string(number)

def STRING_TO_NUM(string):
    return int(string)

def INT(float):
    return int(float)

def ASC(character):
    return ord(character)

print("==============================")
print("Select a function no.")
print("[1] LEFT\n[2] RIGHT\n[3] MID\n[4] LENGTH\n[5] LCASE\n[6] UCASE\n[7] NUM_TO_STRING\n[8] STRING_TO_NUM\n[9] INT\n[10] ASCII")
userchoice = int(input("Select a function number: "))
print("==============================")

if userchoice == 1:
    print("LEFT Function Selected\n")
    string = input("Input String: ")
    length = int(input("Input Length: "))
    print(LEFT(string,length))
elif userchoice == 2:
    print("RIGHT Function Selected\n")
    string = input("Input String: ")
    length = int(input("Input Length: "))
    print(RIGHT(string,length))
elif userchoice == 3:
    print("MID Function Selected\n")
    string = input("Input String: ")
    start = int(input("Start: "))
    end = int(input("End: "))
    print(MID(string,start,end))
elif userchoice == 4:
    print("LENGTH Function Selected\n")
    string = input("Input String: ")
    print(LENGTH(string))
elif userchoice == 5:
    print("LCASE Function Selected\n")
    string = input("Input String: ")
    print(LCASE(string))
elif userchoice == 6:
    print("UCASE Function Selected\n")
    string = input("Input String: ")
    print(UCASE(string))
elif userchoice == 7:
    print("NUM_TO_STRING Function Selected\n")
    number = int(input("Input Number: "))
    print(NUM_TO_STRING(number))
elif userchoice == 8:
    print("STRING_TO_NUM Function Selected\n")
    string = input("Input String: ")
    print(STRING_TO_NUM(string))
elif userchoice == 9:
    print("INT Function Selected\n")
    float = float(input("Input Float: "))
    print(INT(float))
elif userchoice == 10:
    print("ASCII Function Selected\n")
    character = input("Input Character: ")
    print(ASC(character))
