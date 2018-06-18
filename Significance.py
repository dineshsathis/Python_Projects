import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2,f_classif
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LinearRegression, RidgeClassifier
from sklearn.svm import SVR

'''
iris = load_iris()
X, y = iris.data, iris.target
print(X.shape)
print(X)
'''

df=pd.read_excel('C:\Work\Tableau Projects\Clusters.xlsx', sheet_name='Clusters')

X = df[df.columns[1:5]]
y = df[df.columns[0]]
#Recursive Method
'''
estimator = RidgeClassifier()
selector = RFECV(estimator, step=1, cv=5)
selector = selector.fit(X, y)
print(selector.support_)
print(selector.ranking_)
'''

#Select from model method
'''
clf = ExtraTreesClassifier()
clf = clf.fit(X, y)
print(clf.feature_importances_  )
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
print(X.head())
print(X_new)
'''

#Select best method using Chi2 or f_classif
X_new = SelectKBest(f_classif, k=3).fit_transform(X, y)
print(X_new)

