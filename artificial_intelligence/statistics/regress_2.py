import numpy as np
physics_scores = np.array([15,12,8,8,7,7,7,6,5,3])
history_scores = np.array([10,25,17,11,13,17,20,13,9,15])
print(np.polyfit(physics_scores , history_scores,1))

