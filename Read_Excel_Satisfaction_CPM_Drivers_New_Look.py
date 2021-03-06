import pandas as pd
import numpy as np
import os
from scipy.stats import linregress

#Iterate over the immage association and love files, pick the average for each metric for the selected competitor set
#GETS COMPETITOR SET CORRELATION AVERAGE
fpath = "C:\Work\Tableau Projects\New_Look\CPM\Ages_18-34_52w\\"
#df=pd.read_excel(os.path.join(fpath,"Image_Caring-OverTime.xlsx"),1)#Test load to get the column set
#10 competitor set. First brand should be the focus brand
Competitor_Set = ['New Look','Primark','Matalan','Marks & Spencer','Next','Debenhams','Amazon','Asda','Tesco',"Sainsbury's",'H&M','Topshop','Dorothy Perkins','River Island','ASOS','Boohoo','Miss Guided','Zara','Very']
print("Number of retailers in competitor set:" +str(len(Competitor_Set)))
print(Competitor_Set)

'''
#Metric in focus
Metric_Concerned ="PF_Instore_L12M"

#Code to get the correlations
df=pd.read_excel(os.path.join(fpath,"Image_Caring-OverTime.xlsx"),1)#Test load to get the column set
dataframe = pd.DataFrame(columns=df.columns.values)


for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        dataframe = pd.concat ([dataframe, df])

dataframe = dataframe[dataframe["Brand"].isin(Competitor_Set)]#isin requires exact much; double check if all in competitor set is selected.
dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')
dataframe = dataframe.groupby('Data').sum()/len(Competitor_Set)#Divide by number of brands in the competitor set to get average
dataframe = dataframe.transpose()



columns = {'Relationship','slope', 'intercept', 'r_value', 'p_value', 'std_err'}
reg_output_df = pd.DataFrame(columns=columns)

row = 0
column_list = dataframe.columns.values.tolist()
for metric in range(0,len(column_list)):
        dataframe = dataframe.apply(pd.to_numeric)
        qstr = Metric_Concerned + " > 0" #This might throw up an error if the column name has spaces, -, brackets etc. If so, rename columns for a quick fix rather than changing code.
        dataframe = dataframe.query(qstr)
        slope, intercept, r_value, p_value, std_err = linregress(dataframe[Metric_Concerned],dataframe[column_list[metric]])
        reg_output_df.loc[row, 'Relationship'] = Metric_Concerned + " and " + column_list[metric]
        reg_output_df.loc[row, 'slope'] = slope
        reg_output_df.loc[row, 'intercept'] = intercept
        reg_output_df.loc[row, 'r_value'] = r_value
        reg_output_df.loc[row, 'rsq'] = np.power(r_value,2)
        reg_output_df.loc[row, 'p_value'] = p_value
        reg_output_df.loc[row, 'std_err'] = std_err
        row = row + 1

reg_output_df.to_excel("reg_output_" + Competitor_Set[0] + "_"+ Metric_Concerned + "_Ages_18-34" +".xlsx")
'''

'''
#Code to get the rankings for a single day
Latest_Metric_Day = '23/05/2018'

d = {'Brand':['DummyBrand'], 'Data':['DummyImage'], Latest_Metric_Day:[0]}
dataframe = pd.DataFrame(data=d)

for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        try:
                dataframe = pd.concat ([dataframe, df[['Brand','Data', Latest_Metric_Day]]])

        except KeyError:
                print(file + " Key Error")

dataframe = dataframe[dataframe["Brand"].isin(Competitor_Set)]

dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')
dataframe['Image_Rank'] = dataframe.groupby('Data')[Latest_Metric_Day].rank(ascending=False)
dataframe.to_excel(Competitor_Set[0] + "_Metrics_As_Of_" + str(Latest_Metric_Day).replace("/","-") + "_For_Plotting_Ages_18-34.xlsx")
'''

#Code to get the data for multiple days if required

Column_List = ['Brand', 'Data', '12/06/2018']#You can add more dates to pick
dataframe = pd.DataFrame(columns = Column_List)

for file in os.listdir(fpath):
        fname = os.path.basename(file)
        df=pd.read_excel(os.path.join(fpath,fname),1)
        try:
                dataframe = pd.concat ([dataframe, df[Column_List]])

        except KeyError:
                print(file + " Key Error")

dataframe = dataframe[dataframe["Brand"].isin(Competitor_Set)]

dataframe['index'] = np.arange(len(dataframe))
dataframe = dataframe.set_index('index')
#dataframe.to_excel(Competitor_Set[0] + "_Month_End_Days" + "_CPM_For_Plotting_Ages_18-34.xlsx")
dataframe.to_excel(Competitor_Set[0] + "_52w" + "_CPM_For_Plotting_Ages_18-34.xlsx")












