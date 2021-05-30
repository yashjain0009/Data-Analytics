import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
s0=100
r=0.05
sigma=0.25
t=2
i=10000
st1=s0*np.exp((r-0.5*(sigma**2))*t+(sigma*np.sqrt(t)*npr.standard_normal((i))))
st2=s0*npr.lognormal((r-0.5*sigma**2)*t,sigma*np.sqrt(t),size=i)
plt.hist(st2,bins=50)
plt.grid=True
plt.show()