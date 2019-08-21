#!/bin/bash
# displays only the status code of the response
curl -sw "%{http_code}" 0.0.0.0:5000 -o /dev/null 
