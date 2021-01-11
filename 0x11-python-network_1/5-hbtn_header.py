#!/usr/bin/python3
"""
Response header value ( takes in a URL and sends a request to the URL)
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    req = requests.get(argv[1])
    # print(req.headers) --> print dictionary headers information
    print(req.headers.get("X-Request-Id"))
