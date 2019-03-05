import numpy as np
import matplotlib.pyplot as plt

#returns distance between two points
def dist(a,b):
	return np.linalg.norm(a[:,0]-b[:,0])

C1 = np.matrix('1;0')
#C1 is the centre of the given circle
c1 = 0
#c1 is the constant in the equation of given circle
print ("Equation of Circle 1= ||x||^2 - 2",C1.T,"x +",c1,"= 0")
r = ((np.linalg.norm(C1[:,0]))**2-c1)**0.5
#r is the radius of the given Circle
print("Centre 1 = ",C1.T," , radius=",r)
u=np.matrix('1;1')
print ("Equation of Line =", u.T,"x = 3")

#u is normal to given line, hence it is parrallel to C1-C2
alpha = (6-(2*np.matmul(u.T,C1))[0,0])/((np.linalg.norm(u[:,0]))**2)
C2 = C1 + alpha * u
#C2 is the centre of the image circle
c2=(np.linalg.norm(C2[:,0]))**2-r*r
#c2 is the constant in the equation of image circle
print ("Equation of Circle 2= ||x||^2 - 2",C2.T,"x +",c2,"= 0")
print("Centre 2 = ",C2.T," , radius=",r)

A = (C1+C2)/2.0
#A is the midpoint of C1 and C2, lying on line L
AC1 = dist(A,C1)
AC2 = dist(A,C2)
#Will show that A bisects the line C1C2
print("Distances AC1=", AC1, "AC2=",AC2)