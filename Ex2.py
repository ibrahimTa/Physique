import numpy as np 
import matplotlib.pyplot as plt

n=10000
length = 15
width = 3
height = 0.005
nbLines = 10
volumeTot = 0
volumePPs = []

for i in range(n):
    volumeOnePP = 0
    for j in range(nbLines):
        volumeOnePP += np.random.normal(length,0.01) * np.random.normal(width,0.01) * np.random.normal(height,0.001) 
    volumeTot += volumeOnePP       
    volumePPs.append(volumeOnePP)  
    
print("The mean volume is", round((volumeTot/(n)),3), "L")
print("The standard deviation is", round(np.std(np.array(volumePPs)),3), "L")

plt.hist(volumePPs,50)          
plt.show()    