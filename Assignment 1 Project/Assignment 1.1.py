import numpy as np

x = np.array([6,7,8,9,10,11,12])
y = np.array([3,7,11,15,19,23,27])
w = np.array([1,1,0,0.5,1,1.5,2,0,0])
s = np.array([100,98.8,97.6,96.4,95.2])
z = np.array([0.7,1.0,1.3,1.6,1.9,2.2,2.5,2.8])

print(x)
print(y)
print(w)
print(s)
print(z)

v = 3*x+y
print(v)

q = np.dot(x,y)
print(q)

t = (s+4)*np.pi
print(t)

z = z-1
print(z)

xSize = x.size
x[xSize-1] = 4
x[xSize-2] = 4
x[xSize-3] = 4
print(x)

r = 2*w-5
print(r)

M = np.matrix('1,2,3;6,8,4;6,7,5')
N = np.matrix('4,6;7,2;,5,1')
P = np.matrix('2,5;5,5')
print(M)
print(N)
print(P)

A = M*N+N
print(A)

B = N.transpose()*M
print(B)

C = P.I + P
print(C)

#D = A*C*(C+B)
#print(D)

import numpy.linalg as la

Q = la.eig(M)
#R = la.eig(N)
S = la.eig(P)
print(Q)
#print(R)
print(S)