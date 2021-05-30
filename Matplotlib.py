import matplotlib.pyplot as plt
import numpy as np
#plt.figure(figsize=(10, 10))
plt.subplot(221)
plt.title('Graph')
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot(x,y,marker='*',lw=1.9,color='red')
plt.xticks(np.arange(0,50,5))
plt.yticks(np.arange(0,50,10))
plt.grid(True)
plt.subplot(222)
plt.title('Bar Graph')
bar_x=[1,3,4,5,6,8,10]
bar_y=[1,23,32,45,12,4,11]
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.bar(bar_x,bar_y,color='blue')
plt.xticks(np.arange(0,12,1))
plt.yticks(np.arange(0,50,10))
plt.legend(loc=2)
plt.grid(True)
plt.subplot(223)
plt.title('Scatter Graph')
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#z= [1, 4, 3, 2, 7, 6, 9, 8, 10, 5,20, 25, 30, 35]
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.scatter(x,y,marker="*")
#put colourbar plt.colorbar()
plt.subplot(224)
X=200+(5*np.random.rand(4,15))
#plt.figure(figsize=(2,14))
plt.hist(X,10,histtype='bar',label=['1st', '2nd'],stacked=True)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram')
plt.show()
