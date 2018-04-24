# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
#
# # first set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
# line, = ax.plot([], [], lw=2)
#
#
# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,
#
#
# # animation function.  this is called sequentially
# def animate(i):
#     x = np.linspace(0, 2, 1000)
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     return line,
#
#
# # call the animator.  blit=true means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate,
#                                frames=200, interval=20, blit=True)
#attention that 'plt.show' and 'anim.save' functions can not be used simultaneously. I have change the code in __init__.py (at 1062 line) in order to use software 'imagemagick'
# plt.show()
# #anim.save('perceptron2.gif', fps=50, writer='imagemagick')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)
ss = [1,2,3]
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    # xdata.append(frame)
    # ydata.append(np.sin(frame))
    xdata = frame
    ydata = np.sin(frame)
    ln.set_data(xdata, ydata)
    plt.plot(1,0,'o')
    return ln,

anim = FuncAnimation(fig, update, frames=np.linspace(0, np.pi, 128), interval=20,
                    init_func=init, blit=True)
#attention that 'plt.show' and 'anim.save' functions can not be used simultaneously. I have change the code in __init__.py (at 1062 line) in order to use software 'imagemagick'
plt.show()
#anim.save('ping.gif', fps=50, writer='imagemagick')