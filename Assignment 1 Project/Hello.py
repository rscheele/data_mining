from pylab import *
x = np.linspace(0,4*np.pi,100)
noise = np.random.normal(0,0.2,100)
y = np.sin(x) + noise
plot(x, y, '.-r')
title('Sine with gaussian noise')
show()