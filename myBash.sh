#!/bin/bash
echo "First one"
awk -f halfAwk.awk /../../usr/share/dictd/devil.index > items.txt
sort -r items.txt > reverseItems.txt
echo $(head -n 1 reverseItems.txt)

echo "Second one"
awk -f awkProgram.awk /../../usr/share/dictd/devil.index

echo $(time awk -f awkProgram.awk /../../usr/share/dictd/devil.index) 

echo "Third one"
awk -f halfAwk.awk /../../usr/share/dictd/devil.index | sort -r  | head -n 1 | cat

