import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i,x):
    xs = x
    ys = np.arange(0,len(x))
    ax1.clear()
    ax1.plot(xs, ys)

def create_animaton(x):
    ani = animation.FuncAnimation(fig, animate, interval=1000, x = x)
    plt.show()

create_animaton([-0.015748031496062992, -0.015748031496062992, 0.031496062992125984, -0.03937007874015748, -0.06299212598425197, -0.09448818897637795, -0.007874015748031496, -0.015748031496062992, -0.015748031496062992, -0.03937007874015748, 0.047244094488188976, -0.015748031496062992, -0.015748031496062992, -0.047244094488188976, 0.0, 0.007874015748031496, -0.007874015748031496, -0.031496062992125984, -0.03937007874015748, -0.007874015748031496, -0.023622047244094488, 0.0, -0.007874015748031496, -0.023622047244094488, -0.015748031496062992, 0.015748031496062992, -0.023622047244094488, -0.007874015748031496, 0.031496062992125984, 0.031496062992125984, 0.0, -0.023622047244094488, -0.031496062992125984, 0.007874015748031496, 0.023622047244094488, -0.03937007874015748, -0.031496062992125984, -0.05511811023622047, 0.007874015748031496, -0.015748031496062992, -0.023622047244094488, -0.023622047244094488, -0.015748031496062992, -0.007874015748031496, -0.015748031496062992, 0.031496062992125984, -0.023622047244094488, -0.023622047244094488, 0.0, 0.007874015748031496, -0.015748031496062992, 0.0, -0.007874015748031496, 0.015748031496062992, 0.007874015748031496, 0.015748031496062992, 0.0, -0.015748031496062992, -0.05511811023622047, 0.015748031496062992, 0.007874015748031496, 0.023622047244094488, 0.09448818897637795, 0.007874015748031496, 0.199462890625, 0.376220703125, 0.883544921875, -0.19482421875, 0.18292236328125, 0.38336181640625, 0.8828125, -0.20037841796875, -0.54833984375, -0.09375, -0.392578125, -0.53173828125, -0.05615234375, -0.41162109375])