import matplotlib.pyplot as plt
import numpy as np
import random

# Beau graphique random, go Hacktoberfest !

vec = []
vec.append(np.random.normal(100, 0.1,5000))
 

plt.hist(vec,50)          
plt.show()                  

