#!/bin/bash

# learn_predict.bash

# This script should run learn_predict.py for a series of years:

for yr in $(seq 2012 2018)
do
    ~/anaconda3/bin/python learn_predict.py ${HOME}/req/csv/history/TLT_feat.csv $yr 9
done

exit
