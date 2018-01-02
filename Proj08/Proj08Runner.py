#take a list and a character. if the character is found in the item,
# do not copy it. return a list of all items not containing the char.

def run(myList, char):

    print("Jason Burke\n")
    
    print(char)
    print(myList)

    newList = []
    for item in myList:      
        if char not in item:
            newList.append(item)
        
    return newList
