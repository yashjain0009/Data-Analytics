import numpy as np
np.random.seed(1000)
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt
def gen_paths(s0,r,sigma,t,m,i):
    dt=float(t)/m
    paths=np.zeros((m+1,i),np.float64)
    paths[0]=s0
    for t in range(1,M+1):
        rand=np.random.standard_normal(I)
        #rand=(rand-rand.mean())/rand.std()
        paths[t]=paths[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*rand)
        return paths
s0 = 100
r=0.05
sigma = 0.2
T=1.0
M=50
I = 250000
print("ernjvmn")
paths =gen_paths(s0,r,sigma,T,M,I)
print paths[1]
plt.plot(paths[:10, :])
plt.grid(True)
plt.xlabel('time steps')
plt.ylabel('index level')
plt.show()
print ("fkwax")
print (paths[1])
log_returns = np.log(paths[1:] / paths[0:-1])
