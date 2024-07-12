import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math as m

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')

x = np.linspace(0, 2, 500)
x_total = np.concatenate([-x[::-1], x])  

def f(x, a):
    return (x**(2/3)) + (m.e/3) * ((m.pi - x**2)**(1/2)) * np.sin(a * m.pi * x)

linha, = ax.plot([], [], color='red')

def init():
    linha.set_data([], [])
    return linha,

def update(frame):
    a = 0.1 * frame
    y_direita = f(x, a)
    y_total = np.concatenate([y_direita[::-1], y_direita])
    linha.set_data(x_total, y_total)
    print(a)
    return linha,

anim = FuncAnimation(fig, update, frames=200, init_func=init, blit=True)

plt.title("Função: ")
plt.show()
