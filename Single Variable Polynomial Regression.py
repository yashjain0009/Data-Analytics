import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/Users/yashjain/Desktop/data.csv')
df.dropna(inplace=True)
#x=np.empty()
x=np.asarray((df['R&D - March 2014']))
x=x.astype(np.float)
y=np.asarray((df['Revenue+3 March-2017']))
y=y.astype((np.float))

reg=np.polyfit(x,y,deg=2)
ry=np.polyval(reg,x)
#print reg
#plt.subplot(221)
plt.scatter(x,y,marker='*')
#plt.plot(x,ry,'r')
plt.xlabel("R&D")
plt.ylabel("Revenue+3")
plt.grid(True)

z=np.empty(len(x))
for i in range(len(x)):
    z[i]=(-0.24*np.power(x[i],2))+(0.31982744*x[i])+0.01682106
plt.scatter(x,z,marker='.')
error=np.power(np.mean(np.power((ry-y),2)),0.5)
#print z
#print ry
print ("Root Mean Squared Error:\t",error)
plt.show()