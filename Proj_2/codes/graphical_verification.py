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
x1=-7;x2=7
#limits ox x for which line L is being plotted
fig, axes = plt.subplots()
axes.set_xlim(-2,6)
axes.set_ylim(-2,6)
#settig the limits on x and y axis
circle_1 = plt.Circle(C1[:,0],r,fill=False)
axes.add_artist(circle_1)
#plotting given circle
plt.plot(C1[0,0],C1[1,0],'o',label="C1("+str(C1[0,0])+","+str(C1[1,0])+")")
plt.text(C1[0,0]-0.3,C1[1,0]-0.3,'C1')
plt.plot(C2[0,0],C2[1,0],'o',label="C2("+str(round(C2[0,0]))[:7]+","+str(round(C2[1,0]))[:7]+")")
plt.text(C2[0,0]+0.1,C2[1,0]+0.1,'C2')
#plotted the centres of the two circles
plt.plot(A[0,0],A[1,0],'o')
plt.text(A[0,0]-0.1,A[1,0]+0.2,'A')
#plotted the midpoint of C1 and C2, lying on line L
plt.plot((C1[0,0],A[0,0]),(C1[1,0],A[1,0]),label="Line AC1")
plt.plot((C2[0,0],A[0,0]),(C2[1,0],A[1,0]),label="Line AC2")
#plotted lines AC1 and AC2
plt.plot((x1,x2),(3-x1,3-x2),label='Line L: [1 1]x=3')
#plotted line L
circle_2 = plt.Circle(C2[:,0],r,fill=False)
axes.add_artist(circle_2)
#plotted the image circle
plt.xlabel('x');plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.show()