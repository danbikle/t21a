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

'bye'
