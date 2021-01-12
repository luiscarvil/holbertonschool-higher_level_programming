#!/usr/bin/python3
"""
what's my status task (script fetches)
"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    html = req.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
