import datetime
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_url_id_secret():
    return os.getenv("SC_URL"), os.getenv("SC_CID"), os.getenv("SC_CS")


def check_environment_is_correct():
    url, cid, cs = get_url_id_secret()
    if not url:
        raise EnvironmentError("No SC_URL envvar set.")
    if not cid:
        raise EnvironmentError("No SC_CID envvar set.")
    if not cs:
        raise EnvironmentError("No SC_CS envvar set.")


def fetch_sc_token():
    url, cid, cs = get_url_id_secret()
    data = {"grant_type": "client_credentials", "client_id": cid, "client_secret": cs}
    try:
        res = requests.post(url, data=data, timeout=5)
    except:
        raise ConnectionError("Something happened when fetching the token")
    res_dict = json.loads(res.text)
    expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=3500)
    return res_dict["access_token"], expiration_date
