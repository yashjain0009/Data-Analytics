import pandas_datareader as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=web.DataReader(name="^CNXPHARMA",data_source="yahoo",start='2015-01-1',end='2019-12-31')
df=pd.DataFrame(x)
#df=df.tail(20)
#print df
y=web.DataReader(name="AUROPHARMA.NS",data_source="yahoo",start='2019-01-01',end='2019-12-31')
#df2=pd.read_csv('/Users/yashjain/Desktop/^NSEBANK.csv',index_col=0)
df2=pd.DataFrame(y)
#df2=df2.tail(20)
#print df2
fig,ax1=plt.subplots()
df['Return'] = np.log(df['Close'] / df['Close'].shift(1))
df2['Return']= np.log(df2['Close'] / df2['Close'].shift(1))
df['10d Mean']=df["Close"].rolling(window=10).mean()
df['10d Mean']=df2["Close"].rolling(window=10).mean()
df['10d STD']=df["Close"].rolling(window=10).std()
df['10d STD']=df2["Close"].rolling(window=10).std()

print df["10d Mean"]
#df["Close"].plot(xlim=['2020-03-13','2020-03-26'])
#df2["Close"].plot(xlim=['2020-03-13','2020-03-26'])

hdfc=np.asarray(df["Return"].to_list())
bank=np.asarray(df2["Return"].to_list())
plt.plot(hdfc,'r')
ax2=ax1.twinx()
plt.plot(bank)
#reg=np.polyfit(bank,hdfc,deg=7)
#ry=np.polyval(reg,bank)
#plt.plot(bank,hdfc,'b')
#plt.plot(bank,ry,'r')
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.grid(True)
plt.show()