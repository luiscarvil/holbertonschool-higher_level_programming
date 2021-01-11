#!/usr/bin/python3
"""
Response header value ( takes in a URL and sends a request to the URL)
"""
import urllib.request
from sys import argv
req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as req:
    print(req.headers.get("X-Request-Id"))
