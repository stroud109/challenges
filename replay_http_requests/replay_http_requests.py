import requests
import json

from sys import argv

"""
Optimize:
    - abstract kwargs
    - format responses
    - do it asyncronously
"""


def replay_http_requests(input_file_json):

    # print "input file: ", input_file_json

    formatted_requests = json.loads(input_file_json)

    # set up a list for collecting request responses
    responses = []

    # iterate though requests
    for request_attrs in formatted_requests["requests"]:
        # method and url MUST be present
        method = request_attrs["method"]
        url = request_attrs["url"]

        if not (method and url):
            raise Exception  # TODO: figure out a more specific exception

        if method == "GET":
            r = requests.get(url, headers=request_attrs.get("headers"))

        elif method == "POST":
            r = requests.post(url, data=request_attrs.get("body"), headers=request_attrs.get("headers"))

        elif method == "PUT":
            r = requests.put(url, data=request_attrs.get("body"), headers=request_attrs.get("headers"))

        elif method == "PATCH":
            r = requests.patch(url, data=request_attrs.get("body"), headers=request_attrs.get("headers"))

        elif method == "HEAD":
            r = requests.head(url, headers=request_attrs.get("headers"))

        elif method == "DELETE":
            r = requests.delete(url, headers=request_attrs.get("headers"))

        responses.append(r)

    print "responses: ", responses


with open(argv[1]) as input_file:
    replay_http_requests(input_file.read())
