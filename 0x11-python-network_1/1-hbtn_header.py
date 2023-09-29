#!/usr/bin/python3
''' script that take URL senda a request  and displays the value of the 
X-Request-Id variable found in the header of the respons
'''
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.getheaders()).get('X-Request-Id'))
