import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import scipy.stats as scs
def print_statistics(a1, a2):
    sta1 = scs.describe(a1)
    sta2 = scs.describe(a2)
    print (('statistic', 'data set 1', 'data set 2'))
    print 45 * "-"
    print "%14s %14.3f %14.3f" % ('size', sta1[0], sta2[0])
    print "%14s %14.3f %14.3f" % ('min', sta1[1][0], sta2[1][0])
    print "%14s %14.3f %14.3f" % ('max', sta1[1][1], sta2[1][1])
    print "%14s %14.3f %14.3f" % ('mean', sta1[2], sta2[2])
    print "%14s %14.3f %14.3f" % ('std', np.sqrt(sta1[3]), np.sqrt(sta2[3]))
    print "%14s %14.3f %14.3f" % ('skew', sta1[4], sta2[4])
    print "%14s %14.3f %14.3f" % ('kurtosis', sta1[5], sta2[5])
sample_size=500
rn1 = npr.standard_normal(sample_size)
rn2 = npr.normal(100, 20, sample_size)
rn3 = npr.chisquare(df=0.5, size=sample_size)
rn4 = npr.poisson(lam=1.0, size=sample_size)
x0 = 0.05
kappa = 3.0
theta = 0.02
sigma = 0.1
I = 10000
M=50
dt=T/M
def euler:
    xh=np.zeroes((M+1,I))
    x1=np.zeros_like(xh)
    xh[0]=x1[0]=x0
    for t in range(1,M+1):
        xh[t]=kappa*(theta-x0)*dt+(sigma*np.sqrt(x0)*npr.standard_normal(I))