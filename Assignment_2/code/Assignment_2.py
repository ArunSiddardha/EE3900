import numpy as np
A = np.array([[1,-2,3],[-4,2,5]])
B = np.array([[2,3],[4,5],[2,1]])
 
AB= A@B
BA= B@A
print("AB:",AB)
print("BA:",BA)
if AB==BA:
  print("AB = BA")
else :
  print("AB not equal to BA")
