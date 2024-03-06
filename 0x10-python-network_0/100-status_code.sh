#!/bin/bash

# This bash script sends a request to the URL and display only the status code of the response
echo -n $(curl -s -o /dev/null -w "%{http_code}" "$1")


