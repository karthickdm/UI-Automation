#!/usr/bin/env bash

find . -name "*Test.py" -print | while read f; do
        echo "$f"

done
