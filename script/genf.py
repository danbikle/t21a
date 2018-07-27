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
import requests
import sys
import time
import pdb

if (len(sys.argv) != 2):
  print('You should give the name of a CSV-file full of dates and prices.')
  print('Demo:')
  print('~/anaconda3/bin/python genf.py ${HOME}/req/csv/history/TLT.csv')
  sys.exit(1)
    
