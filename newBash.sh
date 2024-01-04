#!/bin/bash

echo "First one"
awk -f awkProgram2.awk /../../usr/share/dictd/devil.index | sort -r | head -n 1 |cat
echo "Second one"
awk -f awkProgram2.awk /../../usr/share/dictd/devil.index | wc -l
