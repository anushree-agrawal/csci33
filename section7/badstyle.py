def bad_style():
    #this isn't that bad bad_style
    d = {}
    d['a'] = 'b'
    try:
        print(d['c'])
    except:
        print("not found!")


bad_style()

import requests

r = requests.get('http://www.google.com')
if r.status_code == 200 or r.status_code == 201:
    print("yay!")
    # keep doing all of your code in here
