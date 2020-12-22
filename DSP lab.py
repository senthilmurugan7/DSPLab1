import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

#============DISCRETE TIME SIGNAL PROCESSING==================

#========Ploting Impulse respose======
n= np.arange(-10,10)
y=(n==0)
stem(n,y)
plt.xlabel("N")
plt.title("Impulse Signal")
plt.xticks(n)
plt.show()
#====================================

#========Ploting Impulse respose======
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem
n= np.arange(-10,10)
#y=[]
#for i in n:
#    if i%2==0:
#        y.append(1)
#    else:
#        y.append(-1)
#y=np.array(y)


y=[1 if i%2==0 else -1 for i in n]


stem(n,y)
plt.xlabel("N")
plt.title("Impulse Signal")
plt.xticks(n)
plt.show()

#===================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem
n= np.arange(-10,10)
y=[1 if i%2==0 else -1 for i in n]
stem(n,y)
plt.xlabel("N")
plt.title("Impulse Signal")
plt.xticks(n)
plt.show()

#=========Step Signal================
n= np.arange(-10,10)
y=(n>0)
stem(n,y)
plt.xlabel("N")
plt.title("Step Signal")
plt.xticks(n)
plt.show()


#=======ramp function===============
y=n*(n>0)
stem(n,y)
plt.xlabel("N")
plt.title("Ramp Signal")
plt.xticks(n)
plt.show()

#=======decreasing function========
y=0.5**n
stem(n,y)
plt.xlabel("N")
plt.title("Decreasing Signal")
plt.xticks(n)
plt.show()

#=======increasing function function======
y=2.0**n
stem(n,y)
plt.xlabel("N")
plt.title("Increasing Signal")
plt.xticks(n)
plt.show()


#=======  exp function =====
y=np.exp(100j*n)
stem(n,y)
plt.xlabel("N")
plt.title("sinusoidal")
plt.xticks(n)
plt.show()


#=============CONTINOUS TIME SIGNAL PROCESSING =================

import matplotlib.pyplot as plt

#====sinwaves at different frequencies=============
t=np.arange(0,4*np.pi,0.001)
f1=10
y = np.sin(10*t)
plt.plot(t,y)
plt.show()

#====Cosine wave  at different frequencies=============
t=np.arange(0,4*np.pi,0.001)
f1=10
y = np.cos(10*t)
plt.plot(t,y)
plt.show()

#====rectified sine wave=============
t=np.arange(0,4*np.pi,0.001)
f1=2
y = 0.5*(np.sin(f1*t)+np.abs(np.sin(f1*t)))
plt.plot(t,y)
plt.show()


#====combining signal=============


t1=np.arange(0,4*np.pi,0.01)
f1=5
y1 = np.sin(f1*t1)

t2=np.arange(0,4*np.pi,0.01)
y2 = 0*np.sin(10*t2)

t3=np.arange(0,4*np.pi,0.01)
f3=10
y3 = np.sin(f3*t3)

y=np.concatenate((y1,y2,y3))
t=np.arange(0,len(y),1)

plt.plot(t,y)
plt.show()


#=========subplot exmaple============

#=======Vertically stacked==============
fig,axis = plt.subplots(2)
axis[0].plot(t1,y1)
axis[0].set_title("plot 0")
axis[1].plot(t1,y2)
axis[1].set_title("plot 1")


#=======Horizontally  stacked==============
fig,(axis1,axis2) = plt.subplots(1,2)
axis1.plot(t1,y1)
axis1.set_title("plot 0")
axis2.plot(t1,y2)
axis2.set_title("plot 1")


#=======Stacking in matrix form==============
fig,ax = plt.subplots(2,2)
ax[0,0].plot(t1,y1)
ax[0,0].plot("plot 0,0")

ax[0,0].plot(t1,y2)
ax[0,1].plot("plot 0,1")

ax[1,0].plot(t1,y3)
ax[1,0].plot("plot 1,0")

ax[1,0].plot(t1,y3)
ax[1,0].plot("plot 1,0")

ax[1,1].plot(t,y)
ax[1,1].plot("plot 1,1")

