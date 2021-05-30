import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2*np.pi,2*np.pi,50)
y= np.sin(x)+0.5*x
reg=np.polyfit(x,y,deg=1)
ry=np.polyval(reg,x)
error=np.sum((y-ry)**2)/len(x)
print reg

plt.subplot(221)
plt.plot(x,y,'b')
plt.plot(x,ry,'r')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend(loc=0)
plt.subplot((222))
matrix=np.zeros((4,len(x)))
matrix[3,:]=x**3
#matrix[3,:]=np.sin(x) for better accuracy since sin term involved
matrix[2,:]=x**2
matrix[1,:]=x
matrix[0,:]=1
reg2=np.linalg.lstsq(matrix.T,y,rcond=None)[0]
ry2=np.dot(reg2,matrix)
plt.plot(x,y,'b')
plt.plot(x,ry2,'r')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
#noisy data
plt.subplot(223)
xn=np.linspace(-2*np.pi,2*np.pi,50)
xn=xn+0.15*np.random.standard_normal(len(x))
yn=(np.sin(xn)+0.5*xn)+0.25*np.random.standard_normal((len(x)))
reg3=np.polyfit(xn,yn,deg=7)
ry3=np.polyval(reg3,xn)
plt.plot(xn,yn,'b')
plt.plot(xn,ry3,'r')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.title(("Noisy Data"))
#radnom data
plt.subplot(224)
xu = np.random.rand(50)*4*np.pi-2*np.pi
yu =np.sin(xu)+0.5*xu
reg4=np.polyfit(xu,yu,deg=5)
ry4=np.polyval(reg4,xu)
plt.plot(xu,yu,'b',marker="*")
plt.plot(xu,ry4,'r',marker="^")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.title("Unsorted Data")
plt.show()

