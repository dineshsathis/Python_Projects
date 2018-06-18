import pandas as pd
import numpy as np
import os

'''
#Read each image association file and select only the H&M and All Brands rows.
fpath = "C:\Work\Tableau Projects\H&M\Image_Associations\\"
df=pd.read_excel(os.path.join(fpath,"Image_Caring-OverTime.xlsx"),1)

row_list = []
for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        df1 = df[(df['Brand'].isin(['H&M','All Brands']))]

        row_list.append(df1.iloc[0])#Get H&M line
        row_list.append(df1.iloc[1])#Get All Brands line

dframe = pd.DataFrame(row_list,columns=list(df.columns.values))
dframe.to_excel("OutHM.xlsx")
print(dframe)
'''

'''
#Read each demand and usage file and select only the H&M and All Brands rows.
fpath = "C:\Work\Tableau Projects\H&M\Demand and Usage Metrics\\"
df=pd.read_excel(os.path.join(fpath,"Purchase Frequency In-Store (L12M)-OverTime.xlsx"),1)

row_list = []
for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        df1 = df[(df['Brand'].isin(['H&M','All Brands']))]

        row_list.append(df1.iloc[0])#Get H&M line
        row_list.append(df1.iloc[1])#Get All Brands line

dframe = pd.DataFrame(row_list,columns=list(df.columns.values))
dframe.to_excel("OutHM.xlsx")
print(dframe)
'''

'''
fpath = "C:\Work\Tableau Projects\H&M\Image_Associations\\"
df=pd.read_excel(os.path.join(fpath,"Image_Caring-OverTime.xlsx"),1)

d = {'Brand':['DummyBrand'], 'Data':['DummyImage'], '27/03/2018':[0]}
dataframe = pd.DataFrame(data=d)

for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        dataframe = pd.concat ([dataframe, df[['Brand','Data', '27/03/2018']]])

dataframe = dataframe[~dataframe["Brand"].isin(['DummyBrand', 'All Brands'])]

dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')

dataframe.to_excel("OutBrands.xlsx")
dataframe['Image_Rank'] = dataframe.groupby('Data')['27/03/2018'].rank(ascending=False)
dataframe.to_excel("OutBrands.xlsx")
'''

'''
#Get the UK
fpath = "C:\Work\Tableau Projects\H&M-UK\Image_Associations\\"
df=pd.read_excel(os.path.join(fpath,"Image_Caring-OverTime (1).xlsx"),1)

dataframe = pd.DataFrame(columns=df.columns.values)

print(dataframe)

for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        dataframe = pd.concat ([dataframe, df])

dataframe = dataframe[~dataframe["Brand"].isin(['All Brands'])]
dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')
dataframe = dataframe.groupby('Data').sum()/17

dataframe.transpose().to_excel("OutDatasetUK1.xlsx")
'''

fpath = "C:\Work\Tableau Projects\US Retailers\Metrics\\"
df=pd.read_excel(os.path.join(fpath,"Visited Overall (LM)-OverTime.xlsx"),1)

dataframe = pd.DataFrame(columns=df.columns.values)

print(dataframe)

for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        dataframe = pd.concat ([dataframe, df])



#dataframe.to_excel("OutMetricsUS_Before_Group.xlsx")
dataframe = dataframe[~dataframe["Brand"].isin(['All Brands'])]
dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')


#Join another dataframe
brandsegmentframe = pd.read_excel("C:\Work\Tableau Projects\US Retailers\Brand_Fast_Slow_Segment.xlsx",1)
dataframe = dataframe.set_index('Brand').join(brandsegmentframe.set_index('Brand'))
dataframe.loc[dataframe['Segment'].isna(), 'Segment'] = 'Other'
fastframe = dataframe[dataframe["Segment"].isin(['Fast'])]
slowframe = dataframe[dataframe["Segment"].isin(['Slow'])]

(fastframe.groupby('Data').sum()/12).transpose().to_excel("Fast_Retailers_US_Sum.xlsx")
#fastframe.groupby('Data').count().transpose().to_excel("Fast_Retailers_US_Count.xlsx")
(slowframe.groupby('Data').sum()/33).transpose().to_excel("Slow_Retailers_US_Sum.xlsx")
#slowframe.groupby('Data').count().transpose().to_excel("Slow_Retailers_US_Count.xlsx")

#Get the average by data metric
#dataframe.groupby(['Data','Segment']).sum().to_excel("Test.xlsx")
#dataframe.groupby(['Data','Segment']).count().to_excel("Test1.xlsx")

#dataframe.transpose().to_excel("OutMetricsUS_After_Group.xlsx")













