import datetime
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class ScToken:
    def __init__(self):
        self._url, self._cid, self._cs = (
            os.getenv("SC_URL"),
            os.getenv("SC_CID"),
            os.getenv("SC_CS"),
        )
        self._token = None
        self.expiry = None
        self._check_environment_is_correct()
        self._init_sc_token()

    def _check_environment_is_correct(self) -> None:
        if not self._url:
            raise EnvironmentError("No SC_URL envvar set.")
        if not self._cid:
            raise EnvironmentError("No SC_CID envvar set.")
        if not self._cs:
            raise EnvironmentError("No SC_CS envvar set.")

    def _init_sc_token(self) -> None:
        data = {
            "grant_type": "client_credentials",
            "client_id": self._cid,
            "client_secret": self._cs,
        }
        try:
            res = requests.post(self._url, data=data, timeout=5)
        except:
            raise ConnectionError("Something happened when fetching the token")
        res_dict = json.loads(res.text)
        self.expiry = datetime.datetime.now() + datetime.timedelta(seconds=3500)
        self._token = res_dict["access_token"]

    @property
    def has_expired(self):
        return self.expiry <= datetime.datetime.now()

    @property
    def string(self):
        if self.has_expired:
            self._init_sc_token()
        return self._token


token = ScToken()
