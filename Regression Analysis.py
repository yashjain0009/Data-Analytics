import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from urllib import urlretrieve
import statsmodels.api as sm
es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
urlretrieve(es_url, '/Users/yashjain/Downloads/Data/es.txt')
urlretrieve(vs_url, '/Users/yashjain/Downloads/Data/vs.txt')
#---optional---
#lines = open('/Users/yashjain/Downloads/Data/es.txt', 'r').readlines()
#lines = [line.replace(' ', '') for line in lines]
#new_file = open('/Users/yashjain/Downloads/Data/es50.txt', 'w')
#new_file.writelines('date' + lines[3][:-1] + ';DEL' + lines[3][-1])
#new_file.writelines(lines[4:])
#new_file.close()
#es = pd.read_csv('/Users/yashjain/Downloads/Data/es50.txt', index_col=0, parse_dates=True, sep=';', dayfirst=True)
#np.round(es)
#es.drop(['DEL'],axis=1,inplace=True)
#es.info()
#---optional---
cols = ['SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF','SXXA', 'DK5F', 'DKXF']
es = pd.read_csv(es_url, index_col=0, parse_dates=True, sep=';', dayfirst=True, header=None,skiprows=4, names=cols)
print (es.tail(5))
vs = pd.read_csv(vs_url, index_col=0, header=2, parse_dates=True, sep=',', dayfirst=True)
data = pd.DataFrame({'EUROSTOXX' :es['SX5E'][es.index > dt.datetime(1999, 1, 1)]})
data = data.join(pd.DataFrame({'VSTOXX' :vs['V2TX'][vs.index > dt.datetime(1999, 1, 1)]}))
data = data.fillna(method='ffill')
print (data.head(5))
#data.plot(subplots=True, grid=True, style='b', figsize=(8, 6))
rets=np.log(data/data.shift(1))
rets.plot(subplots=True,grid=True)
plt.show()
xdat=rets['EUROSTOXX']
ydat=rets['VSTOXX']
model=sm.OLS(ydat,xdat)
print model
#model.summary()
#model=pd.OLS(y=ydat,x=xdat)
#print model
#print model.beta
#model = ols(ydat, xdat).fit()
#print(model.summary())
