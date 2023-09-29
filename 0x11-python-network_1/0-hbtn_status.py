#!/usr/bin/python3
"""code that fetch https://alx-intranet.hbtn.io/status """
import urllib.request


def fetchstate():
    """function to fetch"""
    url = 'https://alx-intranet.hbtn.io/status'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf8')))


if __name__ == "__main__":
    fetchstate()
