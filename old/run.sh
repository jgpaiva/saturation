docker run --rm -i --network="host" peterevans/vegeta sh -c "echo 'GET http://127.0.0.1:8080' | vegeta attack --max-workers 200 -duration 30s | vegeta encode" | jq -r '(.timestamp|sub(".[0-9]+Z$"; "Z")|fromdate|tostring) + "," + (.latency/1000000|tostring)' > www/data/raw_data2.csv
