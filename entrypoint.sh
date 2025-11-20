#!/bin/bash

mkdir -p data
mkdir -p reports

if [ "$1" = "test" ]; then
    echo "Ajetaan Robot Framework testit..."
    shift  # Poistaa argumentin "test"
    robot --console verbose --outputdir /app/reports tests/ "$@"  # loput argumentit robotille
elif  [ "$1" = "shell" ]; then
    echo "Avataan shell ympäristö konttiin..."
    shift  # Poistaa argumentin "shell"
    exec /bin/sh
else
    echo "Running Python application..."
    python ./main.py "$@"
fi