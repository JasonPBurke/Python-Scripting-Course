# Given a word and a tuple, remove any element in the Tuple that
# does not contain the word. return a tuple containing just
# the elements that started with the word given.

import re

def run(myTuple, myWord):

    print("Jason Burke\n")

    print(myWord)
    print(myTuple)

    myLambda = lambda x: re.search(myWord, x)

    returnList = list(filter(myLambda, myTuple))

    return returnList

    

# i need a lambda and need to use filter(function(lambda),sequence(the tuple))
# can use re in the lambda...
