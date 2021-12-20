from __future__ import print_function
import os
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from utils import install_path, optional_environ
import json

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def request():
    try:
        host = optional_environ(
            'CREDS_HOST',
            "http://localhost:5000")
        resp = requests.get(f"{host}/credentials")
        if resp.status_code != 200:
            raise Exception('failed to query credentials')
        return json.dumps(resp.json())
    except Exception as e:
        raise f"Failed to request authentication from {host}. Confirm auth server running. See READ_ME.md for help." from e


def temp_dir():
    return f"{install_path()}/.temp"


def get_creds_try_remote():
    tokens_file = f"{temp_dir()}/token.json"
    try:
        if not os.path.exists(tokens_file):
            msg = f"unable to generate credentials. tokens file not found at {tokens_file}"
            raise Exception(msg)

        creds = Credentials.from_authorized_user_file(tokens_file, SCOPES)
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            save_calendar_tokens(creds.to_json())
        if not creds.valid:
            raise Exception("credentials are not valid, provide new tokens.")
        return creds
    except Exception as e:
        print(f"exception {e} on cred request, requesting from creds host")
        updated = request()
        save_calendar_tokens(updated)
        return Credentials.from_authorized_user_file(tokens_file, SCOPES)


def get_calendar_client():
    service = build('calendar', 'v3', credentials=get_creds_try_remote())
    return service


def get_tokens():
    creds_file = f"{temp_dir()}/credentials.json"
    if not os.path.exists(creds_file):
        raise Exception(
            f"unable to generate tokens, creds file not found at {creds_file}")

    flow = InstalledAppFlow.from_client_secrets_file(
        f"{temp_dir()}/credentials.json", SCOPES,
    )
    creds = flow.run_local_server(port=0)
    return creds


def save_calendar_tokens(creds):
    if creds is None:
        creds = get_tokens().to_json()
    tokens_file = f"{temp_dir()}/token.json"
    with open(f"{tokens_file}", 'w') as token:
        token.write(creds)
    print(f"saved tokens to {tokens_file}")
