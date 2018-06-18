import pandas as pd
import numpy as np
import os

#Iterate over the immage association and love files, pick the rank for each metric for the selected competitor set
#GETS IMAGE RANKING FOR EACH COMPETITOR WITHIN THE SET
fpath = "C:\Work\Relationship Analytics\Satisfaction Analytics\CPM\\"
df=pd.read_excel(os.path.join(fpath,"Satisfaction In-Store-OverTime.xlsx"),1)

d = {'Brand':['DummyBrand'], 'Data':['DummyImage'], '22/04/2018':[0]}
dataframe = pd.DataFrame(data=d)

#Clark's 16 competitor set
Clarks_Competitor_Set = ['Clarks','Adidas','Converse','Kurt Geiger','Marks & Spencer','Next','Nike','Skechers','Zara','Office','Dune','Schuh','Nine West','Aldo','Russell & Bromley','Jones Bootmakers']

for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        dataframe = pd.concat ([dataframe, df[['Brand','Data', '22/04/2018']]])

dataframe = dataframe[dataframe["Brand"].isin(Clarks_Competitor_Set)]

dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')
dataframe['Image_Rank'] = dataframe.groupby('Data')['22/04/2018'].rank(ascending=False)
#dataframe.to_excel("Clarks_Competitorset_Image_Rank_All.xlsx")
dataframe.to_excel("Clarks_Competitorset_Satisfaction_Driver_Ranking_For_Plotting.xlsx")




