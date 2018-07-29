"""
learn_predict.py

This script should read a file full of features,
learn from it and then calculate predictions.

Demo:
cd ~/t21a/script/
~/anaconda3/bin/python learn_predict.py ${HOME}/req/csv/history/TLT_feat.csv
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
  print('You should give the name of a CSV-file full of features.')
  print('Demo:')
  print('~/anaconda3/bin/python genf.py ${HOME}/req/csv/history/TLT_feat.csv')
  sys.exit(1)

# I should get the path of the CSV-file:
file_s = sys.argv[1]

train_df = pd.read_csv(file_s)

train_a = np.array(train_df)[9:]

# I should declare some integers to help me navigate the Arrays.
cdate_i    = 0
cp_i       = 1
pctlead_i  = 2
pctlag1_i  = 3

x_train_a = train_a[:,pctlag1_i:]
y_train_a = train_a[:,pctlead_i]
# I should learn from x_train_a,y_train_a:
from sklearn import linear_model

linr_mod = linear_model.LinearRegression()
linr_mod.fit(x_train_a, y_train_a)

# Now that I have learned, I should predict:

  
'bye'
