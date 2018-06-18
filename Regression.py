import sklearn
import numpy as np
import pandas as pd
import os

import statsmodels.api as sm
from scipy import stats

from sklearn.linear_model import LinearRegression


fpath = "C:\Work\Tableau Projects\H&M\\"
#df=pd.read_excel(os.path.join(fpath,"Regression.xlsx"),0)
df=pd.read_excel(os.path.join(fpath,"Regression.xlsx"),1)

#X = df.drop(['Data','Spend_Instore'],axis=1)
#Y = df['Spend_Instore']
X = df.drop(['Data','Spend_Online'],axis=1)
Y = df['Spend_Online']

#lm = LinearRegression()

X2 = sm.add_constant(X)
est = sm.OLS(Y, X2)
est2 = est.fit()
print(est2.summary())

'''
lm.fit(X,Y)

print (lm.intercept_)

modelview = pd.DataFrame(zip(X.columns,lm.coef_),columns=['Features','Estimated_Coefficients'])

print (modelview)

print(lm.score(X,Y))
'''

