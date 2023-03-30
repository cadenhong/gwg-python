#!/bin/bash

> oldFiles.txt

files=$(grep 'jane ' ../data/list.txt | cut -d ' ' -f 3 | cut -d '/' -f 3)
#grep 'jane ' ../data/list.txt | cut -d ' ' -f 3 | cut -d '/' -f 3
#echo $files

for file in $files; do
  if test -e ../data/$file; then
    echo "$file exists"
    echo "../data/$file" >> oldFiles.txt
  else
    echo "$file doesn't exist"
  fi
done


# This script used to catch all "jane" lines and store them in another text file called oldFiles.txt