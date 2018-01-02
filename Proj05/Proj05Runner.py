
   # this run function will take a string and a subString and check if
   # the subString is found in the string.  It then returns a slice
   # containing three characters preceeding the substring through
   # three characters following the end of the located subString.
   
def run(myString, mySubString):

    print("Jason Burke\n")
    
    print(myString)# print the string to the screen
    print(mySubString)# print the subString to the screen

    subIndex = myString.find(mySubString)# get the index of the subString

    subSize = len(mySubString)# use subSize to +3 to the correct index
    
    mySlice = myString[subIndex-3:(subIndex+subSize)+3]#save the slice

    return mySlice # return the slice of substring + and - 3 chars 

