#/bin/bash
# displays the body of the response
if [ "$(curl -swL \"%{http_code}\" $1 -o /dev/null)" -eq 200 ]; then curl -sL "$1"; fi
