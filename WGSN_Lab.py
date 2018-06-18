import sklearn
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.ensemble import GradientBoostingRegressor as gbr
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston


boston = load_boston()

bos = pd.DataFrame(boston.data)

bos.columns = boston.feature_names

bos['PRICE'] = boston.target

X = bos.drop('PRICE', axis=1)

lm = LinearRegression()

lm.fit(X,bos['PRICE'])

print (lm.intercept_)

modelview = pd.DataFrame(zip(X.columns,lm.coef_),columns=['Features','Estimated_Coefficients'])

print (modelview)


plt.scatter(bos['RM'],bos['PRICE'])
plt.xlabel ('Rooms')
plt.ylabel ('Price')
plt.title ('Rooms vs Price')
plt.show()

'''
X_train,  X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, bos.PRICE,test_size=0.33,random_state=5)

print X_train
print X_test
print Y_train
print Y_test



example = pd.read_csv('C:/Work/Python_Projects/finance_analytics/local_data/Waste_With_Delivery_Offset.csv')


X = example.drop('Waste',axis=1)
Y = example['Waste']

X_train,  X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y,test_size=0.2,random_state=5)
#print X_train
#print X_test
#print Y_train
#print Y_test

lm.fit(X_train,Y_train)
MSE = np.mean((lm.predict(X_test)-Y_test)**2)
#MSE = np.mean((lm.predict(X_train)-Y_train)**2)
print"MR MSE:",MSE, "E:", np.sqrt(MSE)

modelview = pd.DataFrame(zip(X.columns,lm.coef_),columns=['Features','Estimated_Coefficients'])

#print (modelview)
features = [7,352545.7551, 104043.68]

#print(lm.predict(features))

gbr = gbr(n_estimators=10000)
gbr.fit(X_train,Y_train)
MSE = np.mean((gbr.predict(X_test)-Y_test)**2)
#MSE = np.mean((gbr.predict(X_train)-Y_train)**2)
print"BDT MSE:",MSE, "E:", np.sqrt(MSE)


rfr = rfr()
rfr.fit(X_train,Y_train)
MSE = np.mean((rfr.predict(X_test)-Y_test)**2)
#MSE = np.mean((rfr.predict(X_train)-Y_train)**2)
print"RFR MSE:",MSE, "E:", np.sqrt(MSE)



#plt.scatter(rfr.predict(X_test), rfr.predict(X_test)-Y_test)
plt.scatter(rfr.predict(X_train), rfr.predict(X_train)-Y_train)
plt.hlines(y=0,xmin=-5000,xmax=0)
plt.show()


#plt.scatter(gbr.predict(X_test), gbr.predict(X_test)-Y_test)
plt.scatter(gbr.predict(X_train), gbr.predict(X_train)-Y_train)
plt.hlines(y=0,xmin=-5000,xmax=0)
plt.show()
'''



















