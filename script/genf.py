"""
genf.py

This script should generate features from prices and dates.

Demo:
cd ~/t21a/script/
~/anaconda3/bin/python genf.py ${HOME}/req/csv/history/TLT.csv
"""

import datetime
import os
import re
import sys
import time
import pdb
import numpy  as np
import pandas as pd

if (len(sys.argv) != 2):
  print('You should give the name of a CSV-file full of dates and prices.')
  print('Demo:')
  print('~/anaconda3/bin/python genf.py ${HOME}/req/csv/history/TLT.csv')
  sys.exit(1)

# I should get the path of the CSV-file:
file_s = sys.argv[1]

# Assuming the path has slash(s), I should get the name of the CSV-file:
name_l = file_s.split('/')
name_s = name_l[-1]

# I should load the CSV data into a DF
prices_df = pd.read_csv(file_s)

# I should extract date-features:
date_sr = pd.to_datetime(prices_df.Date).dt
# I should extract weekday from Date:
dow_sr = date_sr.dayofweek
# And month of year:
moy_sr = date_sr.month

# I should encode dayofweek and month as binary data:
feat_df = prices_df.copy()[['Date','Close']]
feat_df.columns = ['cdate','cp']
for day_i in range(5):
  feat_df['day'+str(day_i)] = (dow_sr == day_i).astype('int')
min_i = moy_sr.min()
max_i = moy_sr.max()+1
for moy_i in range(min_i,max_i):
  feat_df['moy'+str(moy_i)] = (moy_sr == moy_i).astype('int')

# I should extract price features:
# But first, I should calculate the dependent variable:
feat_df['pct_lead'] = 100.0*((feat_df.cp.shift(-1) - feat_df.cp) / feat_df.cp).fillna(0)

feat_df.head()
'bye'
