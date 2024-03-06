#!/bin/bash

# A bash script to send a request to the URL and display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | tr -d '\n'

