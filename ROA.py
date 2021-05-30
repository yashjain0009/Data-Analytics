from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd
#scaler = preprocessing.StandardScaler()
degree=2
df=pd.read_csv('/Users/yashjain/Library/Preferences/PyCharmCE2019.2/scratches/Process_Dataset.csv')
df.dropna(inplace=True)
#x=np.empty([36,2])
x=pd.DataFrame((df['Research & development expenses']))
x['Size']=df['Size']
x['Current ratio (times)']=df['Current ratio (times)']
x['Debt to equity ratio (times)']=df['Debt to equity ratio (times)']
x=np.asarray(x)
x=x.astype(np.float)
print x.shape
#y=np.empty([36,2])
y=np.asarray(df['Return on total assets'])
y=y.astype((np.float))
#print x
#x_train=np.empty([int((36*0.8)),2])
#y_train=np.empty([int((36*0.8)),2])
#x_test=np.empty([int((36*0.2)),2])
#y_test=np.empty([int((36*0.2)),2])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
lin = LinearRegression()
#print [x_train]
lin.fit(x_train, y_train)
poly = PolynomialFeatures(degree=1)
X_poly = poly.fit_transform(x_train)
poly.fit(X_poly,y_train)
lin2 = LinearRegression()
lin2.fit(X_poly, y_train.reshape(-1,1))
#x_test.reshape(-1,1)
prediction =lin.predict(x_test)
r2=r2_score(y_test,prediction)
print r2
#print y_test
pred=np.empty([64,])
#print prediction
for i in range(0,len(prediction)):
    pred[i]=prediction[i]
#print pred
error=np.power(np.mean(np.power((pred-y_test),2)),0.5)
#es=np.power(error,2)
#error=np.exp(np.mean(np.exp((y_test-prediction),2)),0.5)
print np.mean(y_test)
print ("Root Mean Squared Error:\t",error)
#print x.max()
#print x.shape
#print y.shape
#print x_train.shape
#print y_test.shape