#/bin/bash
# displays the body of the response
[ "$(curl -sIL $1 | grep -e HTTP/1.0\ 200)" ] && curl -sL "$1"
