#!/usr/bin/python3
"""
take URL, sends a request to the URL and display the body of the response
decode in utf-8
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)