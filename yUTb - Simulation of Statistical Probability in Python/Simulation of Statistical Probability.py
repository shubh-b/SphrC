# Probability of getting Head when Tossing a Coin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

space = ['H', 'T']
num = np.arange(10, 10010, 10)
ratio = []
for i in num:
    ratio.append(sum(np.random.choice(space, size=i, replace=True) == 'H')/i)
    
fig, ax = plt.subplots(figsize=[8, 6])

plt.grid()
plt.xlabel("Number of Trials\nwhen Tossing a Coin", fontsize=10)
plt.ylabel("Ratio\n= Number of Heads / Number of Trials\n", fontsize=10)
plt.xticks(np.arange(0, 10100, 100), rotation=50)
plt.yticks(np.arange(0, 1.1, 0.1))

ax.set_xlim(0, (max(num) + 10))
ax.set_ylim(0, 1)

line1, = ax.plot(0, 0, color='red', lw=1)
line2, = ax.plot(0, 0, color='blue', lw=2)

x_data = []
y_data = []
hl_data = []

def anim(i):
    x_data.append(10*i)
    y_data.append(ratio[i])
    hl_data.append(0.5)
    line1.set_xdata(x_data)
    line1.set_ydata(y_data)
    line2.set_xdata(x_data)
    line2.set_ydata(hl_data)    
    return line1, line2,

animate = FuncAnimation(fig, func=anim, frames=num.sort(), interval=10)
plt.show()