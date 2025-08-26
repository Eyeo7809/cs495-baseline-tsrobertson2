def firstUniqueChar(string):
    #Variables to use
    listOfChars = []
    
    #Code
    LCString = string.lower()
    useString = LCString.replace(" ", "")
    for char in useString:
        if char not in listOfChars:
            listOfChars.append(char)
    return(listOfChars)


def main():
   print(firstUniqueChar("Chocolate"))

main()
