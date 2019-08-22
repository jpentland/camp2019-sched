#!/bin/sh
echo "Getting schedule json..."
python3 schedule_camp2019.py > /dev/null
pushd camp2019
python3 parsesched.py $1
