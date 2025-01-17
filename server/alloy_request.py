import os
import requests

EVALUATIONS_API = "https://sandbox.alloy.co/v1/evaluations"
ALLOY_KEY = secret_key = os.environ.get('ALLOY_KEY')

def make_request(data):
    payload = { "name_first": data.get('name_first'), "name_last": data.get('name_last') }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Basic {ALLOY_KEY}"
    }
    response = requests.post(EVALUATIONS_API, json=payload, headers=headers)
    return response.text
