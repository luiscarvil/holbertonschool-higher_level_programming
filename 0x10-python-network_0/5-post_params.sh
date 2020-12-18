#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the pa\
ssed URL, and displays the body of the response
curl -sd "email=hr@holbertonschool.com&subject=I%20will%20always%\
20be%20here%20for%20PLD" "$1"
