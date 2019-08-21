#!/bin/bash
# sends a POST request to the passed URL, and displays the response body
curl -s "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
