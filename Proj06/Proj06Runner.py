
# this run function will split a string and print out each word on its
# own line using whitespace as the delimiter.  then it will split the
# string using the chatacter 'o' as the delimiter

def run(string, seperator):

        print("Jason Burke")# print my name when function called
        print(string)# output the string to the screen
        print(seperator)# output the custom seperator
        
        splitString = string.split(seperator)# split the string using the
                                             # supplied delimiter and save
                                             # the results

        return splitString
