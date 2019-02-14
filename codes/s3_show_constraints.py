import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots()
axes.set_xlim(-4,4)
axes.set_ylim(-4,4)


plt.plot(0,0,'o')
plt.text(0.1,0.1,'A')
plt.plot(1,0,'o')
plt.text(1.1,-0.3,'B')

plt.plot(0,0,'o')
plt.text(-0.4,-0.4,'$C_1$')

circle_1 = plt.Circle((0,0),3,fill=False,linewidth=2)
axes.add_artist(circle_1)

circle_3=plt.Circle((0.5,2**0.5),1.5,fill=False,linewidth=2)
axes.add_artist(circle_3)
plt.plot(0.5,2**0.5,'o')
plt.text(0.5+0.1,2**0.5+0.1,'$C_2$')
plt.plot(0.5,2**0.5,'o')
plt.plot(1,2*(2**0.5),'o')
plt.text(1+0.1,2*(2**0.5)+0.1,'P')
plt.plot((0,1),(0,2*2**0.5),label="$C_1$"+"P=R")
plt.plot((0,0.5),(0,2**0.5),label="$C_2$"+"P="+r"$\alpha$"+"R")


plt.legend()
plt.grid()
plt.show()