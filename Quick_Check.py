import pandas as pd
import numpy as np
import scipy.stats as st
import os
from dateutil.parser import parse

fpath = "C:\Work\Barometer\April_3rd\UK\\"#Folder where metric files from morar are stored
root, dirs, files = os.walk(fpath).next()
fp = fpath + dirs[0]
pd.DataFrame(dirs).to_excel("Folders.xlsx")
pd.DataFrame(os.listdir(fp)).to_excel("Files.xlsx")

