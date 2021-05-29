import requests
from typing import Union

def get_data(url: str) -> Union[str, None]:
    headers = {
        'Accept': 'text/html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    return response.text
