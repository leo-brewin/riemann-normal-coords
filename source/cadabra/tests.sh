#! /bin/bash

echo "---------------------------------------------------------"
echo "> diff text files"
tests-text.sh

echo "---------------------------------------------------------"
echo "> checkpoint files, results in source/cadabra/tests/semantic/summary.pdf"
tests-semantic.sh
