#!/bin/bash
# makes the request to server to get message containing You got me!
curl -sLH "Origin: HolbertonSchool" -X PUT -d "user_id=98" "0.0.0.0:5000/catch_me"
