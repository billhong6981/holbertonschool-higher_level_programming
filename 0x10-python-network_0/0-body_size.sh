#!/bin/bash
# displays the size of the body of the response
curl -sI "$1" | grep -e Content-Length: | cut -d" " -f2
