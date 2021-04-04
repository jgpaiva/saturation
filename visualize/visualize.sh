#!/bin/sh
docker build . -t visualize && cat ../www/data/raw_data2.csv | docker run -i visualize python visualize.py > output.png
