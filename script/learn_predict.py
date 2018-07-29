"""
learn_predict.py

This script should read a file full of features,
learn from it and then calculate predictions.

Demo:
cd ~/t21a/script/
~/anaconda3/bin/python learn_predict.py ${HOME}/req/csv/history/^GSPC_feat.csv 2017
"""

import datetime
import os
import re
import sys
import time
import pdb
import numpy  as np
import pandas as pd

if (len(sys.argv) != 3):
  print('You should give the name of a CSV-file full of features and a year.')
  print('Demo:')
  print('~/anaconda3/bin/python genf.py ${HOME}/req/csv/history/^GSPC_feat.csv 2017')
  sys.exit(1)

# I should get the path of the CSV-file:
file_s = sys.argv[1]
feat_df  = pd.read_csv(file_s) # And read it.
# I should get the year:
yr_s = sys.argv[2]

# I should get the test data using the year:
test_df = feat_df.loc[feat_df.cdate.str.contains(yr_s)]
test_df.head()

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

# I should look at the model:
linr_mod.coef_
linr_mod.intercept_
# Now that I have learned, I should predict:
p_i = 1000 # predictions
test_a        = np.array(test_df)[:,pctlag1_i:]
predictions_a = linr_mod.predict(test_a)
actuals_a     = np.array(test_df)[:,pctlag1_i]
# I should see if model works:
effectiveness = np.sum(np.sign(predictions_a) * actuals_a)
print('effectiveness:')
print(effectiveness)
# I should look at long-only effectiveness:
print('lo_effectiveness:')
print(np.sum(actuals_a))
'bye'
