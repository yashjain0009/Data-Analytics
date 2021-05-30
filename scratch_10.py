import pandas_datareader  as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x=web.DataReader(name="^NSEI",data_source="yahoo",start='2005-1-1')
df=pd.DataFrame(x)
#df.drop(["High"],axis=1,inplace=True)
print df
#plt.plot(x["Date"],x['Close'])
plt.show()