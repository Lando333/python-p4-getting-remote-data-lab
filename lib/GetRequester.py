import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # sends GET resquest to URL passed to init
        response = requests.get(self.url)
        # returns body of response
        return response.content

    def load_json(self):
        # use body to send a request
        # returns list/dict of data from response of request
        return json.loads(self.get_response_body())