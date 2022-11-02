import random
import numpy as np
import matplotlib.pyplot as plt

trials = []
sums = []
def generateData():
    
    for i in range(0,100):
        trials.append(i)
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        sums.append(dice1+dice2)




def calculatePercents():
    percents = {}
    for i in range(len(sums)):
        if sums[i] not in percents:
            percents[sums[i]] = 1
        else:
            percents[sums[i]] = percents[sums[i]] + 1
    
    return percents






fig = plt.figure(tight_layout=True)

ax = fig.add_subplot(2, 2, 1) # using a different approach to arrange plots
      # you need to download the file from the canvas
 # load data from a file
generateData()
col1 = trials        # make array of data in the 1st column
col2 = sums           # make array of data in the 2nd column
ax.scatter(col1, col2, s=1.5, color='green')
ax.set_title("Scatter")
ax.set_xlabel('trial number')
ax.set_ylabel('dice sum')

ax = fig.add_subplot(2, 2, 2)
ax.set_title("Histogram")
ax.set_xlabel('trial number')
ax.set_ylabel('dice sum')
ax.hist(sums)

ax = fig.add_subplot(2, 2, 3)
ax.set_title("Pie Plot")
percents = calculatePercents()
keys = percents.keys()
values = percents.values()
ax.pie(values, labels = keys,autopct='%1.0f%%')

ax = fig.add_subplot(2, 2, 4)
ax.set_title("Line Plot")
ax.set_xlabel('trial number')
ax.set_ylabel('dice sum')
ax.plot(trials,sums)

plt.show()