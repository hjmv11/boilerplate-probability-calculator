import copy
import random
# Consider using the modules imported above.

class Hat:
  #kwargs for unknown number of keyword arguments
  def __init__(self, **kwargs):
    #create content instance variable
    self.contents = []
    #for each key value pair
    for (k, v) in kwargs.items():
      #add the key v number of times
      for i in range(0,v):
        self.contents.append(k)

  #draw n number of balls
  def draw(self, n):
    # if n greater than contents length return all contents, if not pick n number of balls randomly 
    if n >= len(self.contents):
      return self.contents
    else:
      #create list of balls pulled out and copy of original contents
      output = []
      for j in range(0,n):
        #add removed balls to a list 
        output.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
      return output   
  
    
      


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #instantiate count of successful experiments 
  count = 0 

  #do num_experiments
  for i in range(0,num_experiments):
    #create deep copy of hat 
    test_hat = copy.deepcopy(hat)
    
    #draw from copy
    draw = test_hat.draw(num_balls_drawn)
    
    expected_match = True
    #loop through expected balls
    for (k, v) in expected_balls.items():      
      #count of key should be greater than or equal to value, if not set False
      if not draw.count(k) >= v:
        expected_match = False
    #increment count if all count of keys are greater than or equal to values
    if expected_match:
      count += 1

  probability = count/num_experiments
  return probability 