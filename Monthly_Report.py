import pandas as pd
import numpy as np
import scipy.stats as st
import os
from dateutil.parser import parse

fpath = "C:\Work\Barometer\April_29th\UK\\"#Folder where metric files from morar are stored
root, dirs, files = os.walk(fpath).next()
#Update these dates to get the required two months
last_month = "28/04/2018"
previous_month = "31/03/2018"
dfoutput = pd.DataFrame()
global_cols = []

#Create a dataframe with just the metrics on required dates
def createMetric(df, folder, brand):
    new_cols = ['Date']
    Current_Month_Row = 0
    Last_Month_Row = 0
    counter = 0
    global global_cols
    '''
    #Identify the sample size containing columns
    for x in range (1, len(df.columns.values)):
        if( x % 2 == 0):
            cols.append(x)
    #Drop the sample size containing columns
    df.drop(df.columns[cols],axis=1,inplace=True)
    '''

    if len(global_cols)==0:#First time pass. Getting the column list from the first run. No need to do it again
        #Create a composite column name and assign it to dataframe
        for x in range (1,len(df.columns.values)):
            if (x % 2 != 0):#if odd we are in the value column
                created_col_name = str(df.columns[x].split('.')[0]) + ":" + str(df.iloc[0][x]) + ":" + str(df.iloc[1][x]) +":" + str(df.iloc[2][x])
                new_cols.append(created_col_name)#append value column name
                new_cols.append(created_col_name + ":Size")#append size column name
            global_cols = new_cols

    df.columns = global_cols #Attach new column list
    df.drop(df.index[[0,1,2,3]],inplace=True)
    selected_Columns = []
    for a in df.columns:#Only select the date and monthly metrics
        if a.startswith('Monthly') | a.startswith('Date'):
            selected_Columns.append(a)

    df = df[selected_Columns]

    #Identify the rows contianing the dates required
    for row in reversed(range(df.shape[0])):# if the date is equal to wanted date assign it to a row
                    if (parse(df.iloc[row]['Date']).strftime("%d/%m/%Y"))== last_month:
                        df.iloc[row]['Date'] = last_month
                        counter = counter + 1
                        Current_Month_Row = row

                    elif parse(df.iloc[row]['Date']).strftime("%d/%m/%Y")== previous_month:
                        df.iloc[row]['Date'] = previous_month
                        counter = counter + 1
                        Last_Month_Row = row

                    if (counter>1):
                        break

    #Prepate output
    dfoutput = pd.DataFrame(df.iloc[Current_Month_Row]).join(pd.DataFrame(df.iloc[Last_Month_Row]))
    dfoutput.reset_index(level=0, inplace=True)
    dfoutput.columns = dfoutput.iloc[0]
    dfoutput.rename(columns={'Date':'Category'},inplace=True)
    dfoutput["Metric"] = folder
    dfoutput["Brand"] = brand.split('.')[0]

    return dfoutput

dfbrand=pd.read_excel("Select_Brand_Metrics.xlsx",0)
dfbrand = dfbrand[dfbrand.Select==1]
dfmetric=pd.read_excel("Select_Brand_Metrics.xlsx",1)
dfmetric = dfmetric[dfmetric.Select==1]

'''
for folder in range (len(dirs)):#traverse the folders and pick the New Look csv files, extract metrics and append to bottom
    print(dirs[folder])
    fp = fpath + dirs[folder]
    for brand in os.listdir(fp):
            print (brand)
            df = pd.read_csv(os.path.join(fp, brand))#Load only New Look files
            dfoutput = dfoutput.append(createMetric(df,dirs[folder],brand))
'''

for metric in range (len (dfmetric['Metric'])):#traverse the folders and pick the New Look csv files, extract metrics and append to bottom
    fp = fpath + dfmetric['Metric'][metric]
    for brand in range (len(dfbrand['Brand'])):
            print (dfmetric['Metric'][metric] + ":"+ dfbrand['Brand'][brand])
            if os.path.exists(os.path.join(fp, dfbrand['Brand'][brand])):
                df = pd.read_csv(os.path.join(fp, dfbrand['Brand'][brand]))#Load only New Look files
                dfoutput = dfoutput.append(createMetric(df,dfmetric['Metric'][metric],dfbrand['Brand'][brand]))

dfoutput = dfoutput[dfoutput.Category != 'Date']#Remove the row containing 'Date'
dfvalues = dfoutput.loc[~dfoutput.Category.str.endswith('Size')]
dfvalues.index = range(dfvalues.shape[0])
dfsize = dfoutput.loc[dfoutput.Category.str.endswith('Size')]
dfsize.index = range(dfsize.shape[0])

dfoutput = dfvalues.join(dfsize, rsuffix='_Size').drop(columns=['Category_Size', 'Metric_Size', 'Brand_Size'])#Suffixing to get unique columns but dropping duplicates
dfoutput[[last_month,previous_month, last_month+"_Size",previous_month+"_Size"]] = dfoutput[[last_month,previous_month, last_month+"_Size",previous_month+"_Size"]].apply(pd.to_numeric)
dfoutput['Z_Value'] = (dfoutput[previous_month]-dfoutput[last_month])/ np.sqrt(dfoutput[previous_month]*(1-dfoutput[previous_month])/dfoutput[previous_month+"_Size"] + dfoutput[last_month]*(1-dfoutput[last_month])/dfoutput[last_month+"_Size"])
dfoutput['P_Value'] = st.norm.sf(abs(dfoutput['Z_Value']  ))*2
dfoutput['5% Significance'] = dfoutput.apply(lambda row: "Yes" if row['P_Value'] < 0.05 and row['P_Value'] !=0 else "No", axis=1)
dfoutput = dfoutput[['Category','Metric','Brand',last_month, previous_month, last_month+"_Size",previous_month+"_Size",'Z_Value','P_Value', '5% Significance']]
dfoutput.to_excel("Metrics.xlsx")

