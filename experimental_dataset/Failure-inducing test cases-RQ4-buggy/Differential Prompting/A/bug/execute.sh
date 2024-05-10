#!/bin/bash

# Define an array of input file names
inputs=(
    "test_cases_bug/input01.txt"
    "test_cases_bug/input02.txt"
    "test_cases_bug/input03.txt"
    "test_cases_bug/input04.txt"
    "test_cases_bug/input05.txt"
    "test_cases_bug/input06.txt"
    "test_cases_bug/input07.txt"
    "test_cases_bug/input08.txt"
    "test_cases_bug/input09.txt"
    "test_cases_bug/input10.txt"
)

# Loop over the input files and run the four Python scripts on each of them
for input in "${inputs[@]}"; do
    echo "Running scripts on $input..."
    echo "--Buggy--"
    cat "$input" | python buggy.py
    echo "--correct--"
    cat "$input" | python correct.py
    echo "--g1--"
    cat "$input" | python generate1.py
    echo "--g2--"
    cat "$input" | python generate2.py
done
