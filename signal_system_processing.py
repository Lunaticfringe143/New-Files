import numpy as np
import matplotlib.pyplot as plt
#from math import pi as p

amplitude = 0
k = 4/np.pi
m = np.pi/2

t = np.arange(-5, 5, 0.0001)

for i in range(100):
	if i%2 != 0:
		k = (-k/i)*np.cos(i*m*t)
		amplitude = amplitude + k
return amplitude

print(amplitude)



#amplitude = k1+k2+k3+k4+k5

plt.plot(t, amplitude, color='red')
plt.xlabel("Time")
plt.ylabel("amplitude")
plt.suptitle("Periodic Signal")
plt.grid()
plt.show()


#x = np.arange(-12, 12, 0.001)

#y = np.exp(-x*x) #guassian pulse e**-x*x
#y = x*x #parabola

#y = 1+np.sin(x)

#plt.plot(x, y, color='red')
#plt.xlabel("independent")
#plt.ylabel("dependent")
#plt.title("Sample")
#plt.grid()
#plt.show()