#!/bin/bash
for py_file in $(find ./Models/ -name *.py)
do
    python $py_file
done
