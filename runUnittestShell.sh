#!/usr/bin/env bash

#find . -name "*Test.py" -print | while read f; do
#echo "$f"
#cd $HOME/HKEX/workspace/UI/UI-Automation
#python -m unittest Script/ExecuteTest.py
python -m xmlrunner Script/TrialTest.py
#done
