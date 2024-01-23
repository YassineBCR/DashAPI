import requests


def get(endpoint: str, params: dict):
    res = requests.get(url=endpoint, params=params)
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception('ERROR: ' + str(res.content))