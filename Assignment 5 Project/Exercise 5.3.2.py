import numpy as np

''''Table 2'''
xa1 = 105.0
xa2 = 87.0
xb1 = 40.0
xb2 = 62.0
xat = 192.0
xbt = 102.0
x1t = 145.0
x2t = 149.0
xtot = 294.0
''''Table 3 College'''
ya1 = 2.0
ya2 = 9.0
yb1 = 5.0
yb2 = 20.0
yat = 11.0
ybt = 25.0
y1t = 7.0
y2t = 29.0
ytot = 36.0
''''Table 3 Working'''
za1 = 103.0
za2 = 78.0
zb1 = 35.0
zb2 = 42.0
zat = 181.0
zbt = 77.0
z1t = 138.0
z2t = 120.0
ztot = 258.0

OR1 = (xa1/xa2)/(xb1/xb2)
print 'Odd ratio for table 2 is: ' + str(OR1)
OR2 = (ya1/ya2)/(yb1/yb2)
print 'Odd ratio for table 3 college is: ' + str(OR2)
OR3 = (za1/za2)/(zb1/zb2)
print 'Odd ratio for table 3 working is: ' + str(OR3)

phi1 = ((xa1 * xb2) - (xa2 * xb1)) / np.sqrt(xat * xbt * x1t * x2t)
print 'Phi coefficient for table 2 is: ' + str(phi1)
phi2 = ((ya1 * yb2) - (ya2 * yb1)) / np.sqrt(yat * ybt * y1t * y2t)
print 'Phi coefficient for table 3 college is: ' + str(phi2)
phi3 = ((za1 * zb2) - (za2 * zb1)) / np.sqrt(zat * zbt * z1t * z2t)
print 'Phi coefficient for table 3 working is: ' + str(phi3)

ifx = ((xa1+xb2)/xtot)/((xa1 / xtot) * (xb1 / xtot))
print 'Interest factor for table 1 is: ' + str(ifx)
ify = ((ya1+yb2)/ytot)/((ya1 / ytot) * (yb1 / ytot))
print 'Interest factor for table 2 college is: ' + str(ifx)
ifx = ((za1+zb2)/ztot)/((za1 / ztot) * (zb1 / ztot))
print 'Interest factor for table 2 working is: ' + str(ifx)