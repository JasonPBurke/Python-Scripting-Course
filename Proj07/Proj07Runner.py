  #this program takes a string and an index value and splits the string
  # at the index point with an overlap at the index value. We then return
  # index, string, first string split, and the second string split all
  # stored in a list. Main will then print all 4 items to the screen.

def run(string, index):

    print("Jason Burke\n")

    returnString = [index, string, string[:index], string[index-1:]]
    
    return returnString
