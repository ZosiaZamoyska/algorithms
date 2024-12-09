#!/bin/bash

g++ -o generate generate.cpp
g++ -o main main.cpp
g++ -o test test.cpp

for i in {1..1000}; do

    ./generate > input.txt

    ./main < input.txt > output_main.txt
    ./test < input.txt > output_test.txt

    if diff -q output_main.txt output_test.txt > /dev/null; then
        echo "Test $i: OK"
    else
        echo "Test $i: WRONG"
        echo "Input:"
        cat input.txt
        echo "Output from main:"
        cat output_main.txt
        echo "Output from test:"
        cat output_test.txt
        exit 1
    fi
done
