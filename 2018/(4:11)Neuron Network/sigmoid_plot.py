import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x,weight = 1):
    return 1./(1+np.e**(weight*(-x)))

x = np.arange(-6., 6., 0.01)
y = sigmoid(x)
dx = y*(1-y)

fig, ax = plt.subplots(figsize=(7,4))
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Create and show plot
ax.plot(x,y, color="black", linewidth=3, label="sigmoid")
ax.plot(x,dx, color="red", linewidth=3, label="derivative")
ax.legend(loc="upper left", frameon=False)
fig.show()