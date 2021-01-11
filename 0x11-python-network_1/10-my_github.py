#!/usr/bin/python3
"""
script that takes Github credentials (username and password) and uses the Github API to display your id
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv
    req = requests.get("https://api.github.com/users/{}".format(argv[1]),
                       auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get('id'))