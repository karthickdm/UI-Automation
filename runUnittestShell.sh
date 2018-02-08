#!/usr/bin/env bash

find . -name "*Test.py" -print | while read f; do
        echo "$f"
        ###
        python -m coverage run "$f"
        python -m coverage xml -o coverage.xml
        ###
done

cp -r ./coverage.xml /var/lib/jenkins/workspace/example/coverage.xml
cp -r ./python_unittests_xml /var/lib/jenkins/workspace/example/python_unittests_xml