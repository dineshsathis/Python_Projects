import pandas as pd
import numpy as np
import os
from scipy.stats import linregress

'''
#Iterate over the immage association and love files, pick the average for each metric for the selected competitor set
#GETS COMPETITOR SET CORRELATION AVERAGE
fpath = "C:\Work\Tableau Projects\Clarks\Image_Associations\All\\"
df=pd.read_excel(os.path.join(fpath,"Image_Caring-OverTime.xlsx"),1)#Test load to get the column set

dataframe = pd.DataFrame(columns=df.columns.values)

#Clark's 16 competitor set
Clarks_Competitor_Set = ['Clarks','Adidas','Converse','Kurt Geiger','Marks & Spencer','Next','Nike','Skechers','Zara','Office','Dune','Schuh','Nine West','Aldo','Russell & Bromley','Jones Bootmakers']

for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        dataframe = pd.concat ([dataframe, df])


dataframe = dataframe[dataframe["Brand"].isin(Clarks_Competitor_Set)]
dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')
dataframe = dataframe.groupby('Data').sum()/16#Divide by Clark's 16 competitor set to get average
dataframe = dataframe.transpose()

columns = {'Relationship','slope', 'intercept', 'r_value', 'p_value', 'std_err'}
reg_output_df = pd.DataFrame(columns=columns)

row = 0
column_list = dataframe.columns.values.tolist()
for metric in range(0,len(column_list)):
        dataframe = dataframe.apply(pd.to_numeric)
        qstr = "PF_Online_L12M > 0"
        dataframe = dataframe.query(qstr)
        slope, intercept, r_value, p_value, std_err = linregress(dataframe["PF_Online_L12M"],dataframe[column_list[metric]])
        reg_output_df.loc[row, 'Relationship'] = "PF_Online_L12M and " + column_list[metric]
        reg_output_df.loc[row, 'slope'] = slope
        reg_output_df.loc[row, 'intercept'] = intercept
        reg_output_df.loc[row, 'r_value'] = r_value
        reg_output_df.loc[row, 'rsq'] = np.power(r_value,2)
        reg_output_df.loc[row, 'p_value'] = p_value
        reg_output_df.loc[row, 'std_err'] = std_err
        row = row + 1

reg_output_df.to_excel("reg_output_clarks_PF_Online_All.xlsx")
'''



#Iterate over the immage association and love files, pick the rank for each metric for the selected competitor set
#GETS IMAGE RANKING FOR EACH COMPETITOR WITHIN THE SET
fpath = "C:\Work\Tableau Projects\Clarks\Image_Associations\All\\"
df=pd.read_excel(os.path.join(fpath,"Image_Caring-OverTime.xlsx"),1)

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
dataframe.to_excel("Clarks_Competitorset_Latest_Metric_For_Plotting.xlsx")




