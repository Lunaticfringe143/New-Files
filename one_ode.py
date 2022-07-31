import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

def dsdx(x, s):
	y1, y2 = s
	return [y1 + y2**2 + + 3*x,
		 3*y1 +y2**3 - np.cos(x)]
y1_0 = 0
y2_0 = 0

s_0 = (y1_0, y2_0)



x = np.linspace(0, 1, 100)

sol_m1 = odeint(dsdx, y0=s_0, t=x, tfirst=True)


#print(sol_m1)
#print(sol_m2)


y1_sol = sol_m1.T[0]
y2_sol = sol_m1.T[1]

plt.plot(x, y1_sol)
plt.plot(x, y2_sol, '--')
plt.show()
