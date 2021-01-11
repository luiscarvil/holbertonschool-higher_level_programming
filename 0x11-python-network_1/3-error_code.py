#!/usr/bin/python3
"""
take URL, sends a request to the URL and display the body of the response
decode in utf-8
"""
if __name__ == "__main__":
    import urllib.request as request
    import urllib.response as response
    import urllib.error as error
    from sys import argv
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as re:
            print(re.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
