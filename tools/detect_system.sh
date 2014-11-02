#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform
    echo "MAC"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under Linux platform
    echo "Linux"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    # Do something under Windows NT platform
    echo "Windows"
fi
