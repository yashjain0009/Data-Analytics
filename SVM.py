import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from  sklearn.metrics import accuracy_score
iris= datasets.load_iris()
x=iris.data
y=iris.target
print x
model=svm.SVC()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model.fit(x_train,y_train)
prediction =model.predict(x_test)
acc=accuracy_score(y_test,prediction)

print("predictions",prediction)
print ('actual:',y_test)
print("accuracy",acc)