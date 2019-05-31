import numpy as np
import matplotlib.pyplot as plt

men_means = (20, 35, 30, 35, 27)
women_means = (25, 32, 34, 20, 25)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars
plt.figure(figsize=(8,6))
fig, ax = plt.subplots()

rects1 = ax.bar(ind - width / 2, men_means, width, color='SkyBlue', label='Men')
rects2 = ax.bar(ind + width / 2, women_means, width, color='IndianRed', label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()

plt.show()
