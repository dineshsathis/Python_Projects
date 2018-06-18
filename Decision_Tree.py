import sklearn
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_boston

boston = load_boston()

#Following code outputs a dataframe to Excel
bos = pd.DataFrame(boston.data)
writer = pd.ExcelWriter('output.xlsx')
bos.to_excel(writer,'Sheet1')
writer.save()

bos.columns = boston.feature_names

bos['PRICE'] = boston.target

X = bos.drop('PRICE', axis=1)

#dt = tree.DecisionTreeClassifier(criterion='gini')
dt = tree.DecisionTreeRegressor()

dt.fit(X,bos['PRICE'])

#dt.score(X,bos['PRICE'])

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import pydot
from graphviz import Source
dot_data = StringIO()
export_graphviz(dt, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True)

graph = Source( tree.export_graphviz(dt, out_file=None, feature_names=X.columns))
graph.format = 'png'
graph.render('dtree_render',view=True)

#Below line outputs text file tree. Paste the contents to Webgraphviz.
#tree.export_graphviz(dt,out_file='tree.dot')




'''
plt.scatter(bos['RM'],bos['PRICE'])
plt.xlabel ('Rooms')
plt.ylabel ('Price')
plt.title ('Rooms vs Price')
plt.show()


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



















