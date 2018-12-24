#!/bin/bash
# Leetcode test suite
# Arthur Dysart
#
# INSTRUCTIONS
# Run bash script to check test cases for this directory.
# 
# EXAMPLE
# bash python_tests.sh


## FUNCTION DEFINITIONS
function create_test_directory {
  ## Creates temporary directory for test cases
  mkdir ./temp
}

function execute_tests {
  ## Executes all test cases from input and output directories
  for TEST in ./input/*.txt ; do
    # Identifies test case files
    TEST_NUM=${TEST//[^0-9]/}
    INPUT=./input/input${TEST_NUM}.txt
    RESULT=./temp/temp${TEST_NUM}.txt
    OUTPUT=./output/output${TEST_NUM}.txt

    # Executes selected test case and saves result
    python.exe python_source.py < ${INPUT} > ${RESULT}
    
    # Compares result with expected output
    DIFF="$(diff -ZB ${RESULT} ${OUTPUT})"
    NAME="$(basename $(pwd))"
    if [ "${DIFF}" ] ; then
      echo -e "${NAME}    Test ${TEST_NUM}    FAIL\n"
      echo -e "${DIFF}\n"
    else
      echo -e "${NAME}    Test ${TEST_NUM}    SUCCESS\n"
    fi
  done
}

function remove_test_directory {
  ## Deletes temporary directory for test cases
  rm -r ./temp
}

## MAIN MODULE
main() {
    create_test_directory
    execute_tests
    remove_test_directory
}

main