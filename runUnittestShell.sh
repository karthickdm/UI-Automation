#!/usr/bin/env bash

#find . -name "*Test.py" -print | while read f; do
#echo "$f"
#cd $HOME/HKEX/workspace/UI/UI-Automation
python -m unittest Script/TrialTest.py
echo $?
#done
