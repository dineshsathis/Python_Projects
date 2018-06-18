import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df=pd.read_excel('C:\Work\Tableau Projects\Macys\Macys.xlsx', sheet_name='Profiles')
print(df.shape[0])


X = df[['P_Age', 'P_Dress_size_female', 'P_Household_Income']]
print(X.shape[0])
#X_Cleaned_Selected = X[['P_Age', 'P_Dress_size_female', 'P_Household_Income']].dropna()
X_Cleaned_Selected = X[['P_Age', 'P_Household_Income']].dropna()
#print(X_Cleaned_Selected.head(5))
scaler = StandardScaler()
X_scaled = scaler.fit_transform( X_Cleaned_Selected )


#Find the elbow: Ideal number of clusters

cluster_range = range( 1, 20 )
cluster_errors = []

for num_clusters in cluster_range:
  clusters = KMeans( num_clusters )
  clusters.fit( X_scaled )
  cluster_errors.append(clusters.inertia_)
clusters_df = pd.DataFrame( { "num_clusters":cluster_range, "cluster_errors": cluster_errors } )

#Check the elbow
plt.figure(figsize=(12,6))
plt.plot( clusters_df.num_clusters, clusters_df.cluster_errors, marker = "o" )
plt.show()


#Use the ideal number of clusters
cluster = KMeans(6)
cluster.fit(X_scaled)

#Add cluster label back to original dataframe
X_Cleaned_Selected["Cluster"] = cluster.labels_

#Plot clusters
ax = plt.axes(projection='3d')
cm = plt.get_cmap("RdYlGn")

ax.scatter3D(X_Cleaned_Selected["P_Age"], X_Cleaned_Selected["P_Dress_size_female"], X_Cleaned_Selected["P_Household_Income"], c=X_Cleaned_Selected["Cluster"],cmap=cm)
plt.show()

#Save to file
writer = pd.ExcelWriter('cluster_output.xlsx')
X_Cleaned_Selected.to_excel(writer,'Sheet1')
writer.save()









