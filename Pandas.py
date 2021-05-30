# importing pandas as pd
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn import datasets
import matplotlib.pyplot as plt
# Making data frame from the csv file
df = pd.read_csv('/Users/yashjain/Desktop/data.csv')
#RD=df['R&D - March 2014'].dropna()
#REV=df['Revenue+3 March-2017']
#df2=pd.DataFrame(df['R&D - March 2014'],,df['Revenue+3 March-2017'])
df.dropna(inplace=True)

x=pd.DataFrame(df['R&D - March 2014'])
x['R&D - March 2015']=df['R&D - March 2015']
y=pd.DataFrame(df['Revenue+3 March-2017'])
print x

reg=np.polyfit(x,y,deg=4)
ry=np.polyval(reg,x)
plt.plot(x,y,'b')
plt.plot(x,ry,'r')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend(loc=0)
plt.show()

print y.head()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2)
l_reg=linear_model.LinearRegression()
model=l_reg.fit(x_train,y_train)
prediction=l_reg.predict(x_test)
coeff=l_reg.coef_

#y_test2=np.asarray(y_test['ANNUAL RETURN+2'])
##pred=np.empty([len(prediction)])
for x in prediction:
    np.append(pred,x)
print pred
print np.shape(pred)
print np.shape(y_test2)
#print r2_score(y_test,prediction)
#acc= accuracy_score(y_test2,pred)
#print acc

print coeff