#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) < 2 or len(argv) > 2:
        q = ""
    else:
        q = argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_dict_json = req.json()
        # print(req_dict_json)
        id = req_dict_json.get('id')
        # print(id)
        name = req_dict_json.get('name')
        # print(name)
        if len(req_dict_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(
                req_dict_json.get('id'), req_dict_json.get('name')))
    except Exception:
        print("Not a valid JSON")
