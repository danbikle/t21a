"""
reqp.py

This script should request prices.

Demo:
cd ~/t21a/script/
~/anaconda3/bin/python reqp.py tkrlist.txt
"""

import datetime
import os
import re
import requests
import sys
import time
import pdb

if (len(sys.argv) != 2):
  print('You should give the name of a file full of tickers.')
  print('Demo:')
  print('~/anaconda3/bin/python reqp.py tkrlist.txt')
  sys.exit(1)
    
tkrs_s = sys.argv[1]

# I should ensure the output folders exist
outdirh = '${HOME}/req/html/'
os.system('mkdir -p '+outdirh)

csv_types_l = ['history']

os.system('mkdir -p ${HOME}/req/csv/history')

# I should prepare to talk to Yahoo:
yahoo_s      = 'https://finance.yahoo.com/quote/'
user_agent_s = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
headers_d    = {'User-Agent': user_agent_s}
ycsv_s       = 'https://query1.finance.yahoo.com/v7/finance/download/'
nowutime_s   = datetime.datetime.now().strftime("%s")
params_s     = '?period1=-631123200&period2='+nowutime_s+'&interval=1d&events='

def get_tkr():
  """This function should get CSV data for a tkr and return a status of that attempt."""
  type_s    = 'history'
  history_s = yahoo_s+tkr+'/history?p='+tkr
  with requests.Session() as ssn:
    tkr_r   = ssn.get(history_s,headers=headers_d)
    html_s  = tkr_r.content.decode("utf-8")
    # with open(outdirh+tkr+'.html','w') as fh:
    with open('req/html/'+tkr+'.html','w') as fh:
      fh.write(html_s)
    pattern_re = r'(CrumbStore":{"crumb":")(.+?")'
    pattern_ma = re.search(pattern_re, html_s)
    crumb_s    = pattern_ma[2].replace('"','') # erase " on end of crumb
    print('crumb_s:')
    print(crumb_s)
    # for type_s in csv_types_l:
    csvurl_s = ycsv_s+tkr+params_s+type_s+'&crumb='+crumb_s
    # yahoo server needs time to remember the cookie-crumb-pair it just served:
    time.sleep(5)
    csv_r        = ssn.get(csvurl_s,headers=headers_d)
    csv_status_i = csv_r.status_code
    if (csv_status_i == 200) :
      # I should write the csv_s to csv file:
      csv_s  = csv_r.content.decode("utf-8")
      csvf_s = 'req/csv/'+type_s+'/'+tkr+'.csv'
      with open( csvf_s,'w') as fh:
        fh.write(csv_s)
        print('wrote: ', csvf_s)
    else:
      print(tkr, type_s, 'status not 200 for some reason')
  return csv_status_i

# I should use tkrlist.txt drive a loop

# I get csv from URL like this:
# https://query1.finance.yahoo.com/v7/finance/download/AA?period1=1492462308&period2=1495054308&interval=1d&events=history&crumb=pYheK5rafih

with open(tkrs_s) as fh:
  tkrlist_s   = fh.read()
  tkrlist_l   = tkrlist_s.split()
  for tkr in tkrlist_l:
    csv_status_i = get_tkr()
    if csv_status_i == 200:
      'be happy'
    else:
      'try again'
      csv_status_i = get_tkr()
      if csv_status_i == 200:
        'be happy'
      else:
        'try 3rd time, the last time'
        csv_status_i = get_tkr()
'bye'
