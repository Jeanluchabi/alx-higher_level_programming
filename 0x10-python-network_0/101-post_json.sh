#!/bin/bash

# This is a bash script that sends a JSON POST request to a URL passed as the first argument
# Usage: ./script.sh <URL> <filename>

# Send a JSON POST request to the URL with the contents of a file specified by the second argument as the request body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"


