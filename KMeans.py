import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df=pd.read_excel('C:\Work\Barometer\Dataset\profiles-UK.xlsx', sheet_name='profiles-UK')
print(df.shape[0])


X = df[['Age', 'Dress_size_female', 'Household_Income', 'Income Filter', 'Size Filter']]
print(X.shape[0])
#X_Cleaned = X[( (X['Dress_size_female']>=0) & (X['Dress_size_female']<=6) & (X['Household_Income']>=0) & (X['Household_Income']<=100000) )]
X_Cleaned = X[(X['Income Filter']==True) & (X['Size Filter']==True) ]
X_Cleaned_Selected = X_Cleaned[['Age', 'Dress_size_female', 'Household_Income']].dropna()
#print(X_Cleaned_Selected.head(5))
scaler = StandardScaler()
X_scaled = scaler.fit_transform( X_Cleaned_Selected )


#Find the elbow: Ideal number of clusters
'''
cluster_range = range( 1, 20 )
cluster_errors = []

for num_clusters in cluster_range:
  clusters = KMeans( num_clusters )
  clusters.fit( X_scaled )
  print(clusters.inertia_)
'''

#Use the ideal number of clusters
cluster = KMeans(6)
cluster.fit(X_scaled)

#Add cluster label back to original dataframe
X_Cleaned_Selected["Cluster"] = cluster.labels_

writer = pd.ExcelWriter('cluster_output.xlsx')
X_Cleaned_Selected.to_excel(writer,'Sheet1')
writer.save()








