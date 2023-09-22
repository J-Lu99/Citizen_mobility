#!/bin/bash

nohup python3 'Matrix&Hist.py' unst &
wait

nohup python3 'Matrix&Hist.py' st &
wait

nohup python 3 'Means.py' all &
nohup python 3 'Means.py' week &


