import json
import os

import requests
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from ScToken import token

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def authorized_get(url_params: str):
    def compose_final_url(after_slash: str):
        base_url = os.getenv("SC_API_BASE_URL")
        if not base_url:
            raise EnvironmentError("No SC_API_BASE_URL envvar set.")
        return f"{base_url}/{after_slash}"

    return requests.get(
        compose_final_url(url_params),
        headers={"Authorization": f"OAuth {token.string}"},
    )


@app.route("/<int:track_id>")
def track(track_id):
    res = authorized_get(track_id)
    return json.loads(res.text)


@app.route("/<int:track_id>/stream")
def track_stream(track_id):
    res = authorized_get(f"{track_id}/stream")
    return res.content


if __name__ == "__main__":
    app.run()
