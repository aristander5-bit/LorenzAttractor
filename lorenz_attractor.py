import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def lorenz(t, state, sigma=10.0, rho=28.0, beta=8.0 / 3.0):
  x, y, z = state
  dxdt = sigma * (y - x)
  dydt = x * (rho - z) - y
  dzdt = x * y - beta * z
  return [dxdt, dydt, dzdt]

from scipy.integrate import solve_ivp

sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
state0 = [1.0, 1.0, 1.0]
t_span = (0, 40)
t_eval = np.linspace(0, 40, 10000)

sol = solve_ivp(lorenz, t_span, state0, t_eval=t_eval)


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(projection="3d")


ax.plot(sol.y[0], sol.y[1], sol.y[2], lw=0.5, color="b")

ax.set_title("Атрактор на Лоренц")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()