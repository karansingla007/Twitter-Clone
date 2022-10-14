import requests
import json

from twitter_api.utils.constants import BEARER_TOKEN

bearer_token = BEARER_TOKEN


def create_url(usernames):
    user_fields = "user.fields=description,created_at"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def fetchTwitterUserDetailByUserName(usernames):
    url = create_url(usernames)
    json_response = connect_to_endpoint(url)
    return json_response
