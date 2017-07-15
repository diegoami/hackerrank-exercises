import numpy as np
physics_scores = np.array([15,12,8,8,7,7,7,6,5,3])
history_scores = np.array([10,25,17,11,13,17,20,13,9,15])
a,b = np.polyfit(physics_scores , history_scores,1)
print(a*10+b)

