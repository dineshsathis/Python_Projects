import pandas as pd
import os
from dateutil.parser import parse

dataframe=pd.read_excel("New_Look_Competitor_Satisfaction.xlsx",0,index_col=False)
dataframe['Score_Rank'] = dataframe.groupby('Metric')['Score'].rank(ascending=False)
dataframe.to_excel("CPM_Rank_52w.xlsx")