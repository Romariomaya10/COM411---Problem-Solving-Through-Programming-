import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(frame):
  print(f"Frame Number is {frame}")


def run():

 fig, ax = plt.subplots()
 some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 1000)

 
 plt.show()


run() 
