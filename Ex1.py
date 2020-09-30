import matplotlib.pyplot as plt
import numpy as np
import random

vec = []
i = 0
while i < 50:
    error = random.uniform(0,2)
    if random.randint(0, 1) % 2 == 0 :
        vec.append(100-error)
    else:
        vec.append(100+error)
    i += 1

print(vec)
 
plt.hist(vec,25)          
plt.show()                  