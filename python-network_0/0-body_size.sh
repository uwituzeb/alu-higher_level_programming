#!/bin/bash
# sends a request an URL, and displays the size of the body of the response

curl -sL "$1" | grep 'Content-Length' | awk '{print $2}'
