#!/bin/bash

# This a bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sLX PUT 0.0.0.0:5000/catch_me --data "user_id=98" -H "Origin: HolbertonSchool"
