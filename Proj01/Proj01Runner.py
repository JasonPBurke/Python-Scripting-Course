import turtle

class Runner:

   print("Jason Burke")
	
   def run(myTuple):

      #add pensize,color, shape to first incomming turtle object
      myTuple[0].pensize(2)
      myTuple[0].color('red')
      myTuple[0].shape('turtle')
      #add pensize,color, shape to second incomming turtle object
      myTuple[1].pensize(3)
      myTuple[1].color('green')
      myTuple[1].shape('circle')
      #add pensize,color, shape to third incomming turtle object
      myTuple[2].pensize(4)
      myTuple[2].color('blue')
      myTuple[2].shape('triangle')
      #create a name object to return as the 4th object in the list		
      name = "Jason Burke"
      #add the 3 modified turtle objects and name to a list
      myList = [ myTuple[0], myTuple[1], myTuple[2], name ]
      # return the 4 object list
      return myList
