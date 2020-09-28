""" Making Pseudocode real. Create the Pseudocode in Python.
By the way this is NOT a nice way to name your definitions in Python, but it 
lets you get away with it.
pass lets me not code up the function. It's like on a quiz show.
"""

def LEFT(string,length): #done  
    # returns the left most characters of a string. 
    # I've done this one as an example.
    return string[0:length]

def RIGHT(string,length): #done
    # Returns the right most characters of a string
    return string[-length:]

def MID(string,start,end): #done
    # Returns string from position x, length y. Note that the count starts at 1. 
    return string[start-1:end]
    
def LENGTH(string): #done
    #Returns the lengths of a string
    return len(string)

def LCASE(string): #done
    #From here on in you need to figure out the parameters and the function.    
    return string.lower()
    
def UCASE(string): #done
    #Returns the upper case character. (Does nothing if already upper case). Note that this works on characters rather than a string.
    return string.upper()

def TO_UPPER(string):
    #Returns a string in upper class. (Non-alphabetic characters and upper case characters remain unchanged)
    return string.upper()
 
def TO_LOWER(string):
    #Returns a string in lower class. (Non-alphabetic characters and lower case characters remain unchanged)
    return string.lower()
 
def NUM_TO_STRING(number):
    return string(number)

def STRING_TO_NUM(string):
    return int(string)

def INT(float):
    return int(float)

def ASC(character):
    #Changes a character into its ASCII number.
    return ord(character)

print("==============================")
print("Select a function no.")
print("[1] LEFT\n[2] RIGHT\n[3] MID\n[4] LENGTH\n[5] LCASE\n[6] UCASE\n[7] NUM_TO_STRING\n[8] STRING_TO_NUM\n[9] INT\n[10] ASC")
userchoice = int(input("Select a function number:"))

if userchoice == 1:
