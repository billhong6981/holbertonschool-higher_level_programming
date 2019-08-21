#/bin/bash
# displays the body of the response
if [ "$(curl -sIL $1 | grep -e HTTP.*200)" ]; then curl -sL "$1"; fi
