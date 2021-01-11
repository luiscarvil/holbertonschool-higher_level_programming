#!/usr/bin/python3
"""
takes in a URL and an email sends a POST request to the passed URL
with the email as a parameter
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    mail = {'email': argv[2]}
    data = parse.urlencode(mail).encode('utf-8')
    # print(data) --> b'email=hr%40holbertonschool.com'
    req = request.Request(argv[1], data)
    # print(req) --> <urllib.request.Request object at 0x7f6b9a926fd0>
    # print(type(req)) --> <class 'urllib.request.Request'>
    with request.urlopen(req) as re:
        print(re.read().decode('utf-8'))
