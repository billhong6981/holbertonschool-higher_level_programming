#!/bin/bash
# displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep Allow: | sed 's/Allow: //'

