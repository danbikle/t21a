#!/bin/bash

# learn_predict.bash

# I should ensure that I have the features I want:

export TKR=^GSPC
~/anaconda3/bin/python genf.py ${HOME}/req/csv/history/${TKR}.csv

# This script should run learn_predict.py for a series of years:

for yr in $(seq 2000 2018)
do
    ~/anaconda3/bin/python learn_predict.py ${HOME}/req/csv/history/${TKR}_feat.csv $yr 25
    echo oooooooooooooooooooooooooooooooooooo
done

exit
