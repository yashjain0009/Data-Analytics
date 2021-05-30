from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
import matplotlib.pyplot as plt
boston = datasets.load_boston()
x=boston.data
y=boston.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2)
l_reg=linear_model.LinearRegression()
model=l_reg.fit(x_train,y_train)
prediction=model.predict(x_test)
coeff=l_reg.coef_
print coeff
print y_test
#acc=accuracy_score(y_test,prediction)

