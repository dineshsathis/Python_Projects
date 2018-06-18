import pandas as pd
import os
from dateutil.parser import parse

fpath = "C:\Work\Barometer\May_6th\UK\\"#Folder where metric files from morar are stored
root, dirs, files = os.walk(fpath).next()
#Update these dates to get the required two months
Months = ["06/05/2018", "28/04/2018", "21/04/2018", "14/04/2018", "07/04/2018", "31/03/2018", "24/03/2018", "17/03/2018", "10/03/2018", "03/03/2018", "24/02/2018", "17/02/2018", "10/02/2018", "03/02/2018", "27/01/2018", "20/01/2018", "13/01/2018", "06/01/2018", "30/12/2017", "23/12/2017", "16/12/2017"]
dfoutput = pd.DataFrame()
global_cols = []

#Create a dataframe with just the metrics on required dates
def createMetric(df, folder, brand):
    new_cols = ['Date']
    Current_Month_Row = 0
    Last_Month_Row = 0
    Month_Rows = []
    counter = 0
    global global_cols

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
        if a.startswith('12 Week Average') | a.startswith('Date'):
            selected_Columns.append(a)

    df = df[selected_Columns]

    #Identify the rows contianing the dates required
    for row in reversed(range(df.shape[0])):# if the date is equal to wanted date assign it to a row
        for month in range(len(Months)):
                    if (parse(df.iloc[row]['Date']).strftime("%d/%m/%Y"))== Months[month]:
                        df.iloc[row]['Date'] = Months[month]
                        counter = counter + 1
                        Month_Rows.append(row)

                    elif parse(df.iloc[row]['Date']).strftime("%d/%m/%Y")== Months[month]:
                        df.iloc[row]['Date'] = Months[month]
                        counter = counter + 1
                        Month_Rows.append(row)

                    if (counter>len(Months)):#After we find the months required let STOP
                        break


    dfoutput = df.iloc[Month_Rows].transpose()
    dfoutput.reset_index(level=0, inplace=True)
    dfoutput.columns = dfoutput.iloc[0]
    dfoutput.rename(columns={'Date':'Category'},inplace=True)
    dfoutput["Metric"] = folder
    dfoutput["Brand"] = brand.split('.')[0]#Brand.csv is split by dot and first item which is the name is selected

    return dfoutput



dfbrand=pd.read_excel("Select_Brand_Metrics.xlsx",0,index_col=False)
dfbrand = dfbrand[dfbrand.Select==1]
dfbrand.reset_index(level=0, inplace=True)

dfmetric=pd.read_excel("Select_Brand_Metrics.xlsx",1,index_col=False)
dfmetric = dfmetric[dfmetric.Select==1]
dfmetric.reset_index(level=0, inplace=True)

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

dfoutput = dfvalues.join(dfsize, rsuffix='_Sample_Size').drop(columns=['Category_Sample_Size', 'Metric_Sample_Size', 'Brand_Sample_Size'])#Suffixing to get unique columns but dropping duplicate value columns
dfoutput = dfoutput.apply(pd.to_numeric, errors='ignore')
dfMetricSplit= dfoutput['Category'].str.split(':', expand=True)
dfoutput = dfoutput.join(dfMetricSplit)
dfoutput.rename(columns={0: 'Metric_Period', 1: 'Region', 2: 'Age', 3: 'Economic_Segment'}, inplace=True)

columns = dfoutput.columns.values.tolist()
remove_list = ['Category', 'Metric', 'Brand', 'Metric_Period', 'Region', 'Age', 'Economic_Segment']
for x in range(len(remove_list)):
    columns.remove(remove_list[x])

dfoutput = pd.melt(dfoutput, id_vars=['Metric', 'Region', 'Age', 'Economic_Segment'], value_vars=columns, var_name='Period', value_name='Metric_Value')
dfoutput.to_excel("Metrics_Next.xlsx")






