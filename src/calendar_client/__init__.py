from __future__ import print_function
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from utils import install_path


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def temp_dir():
    return f"{install_path()}/.temp"


def get_calendar_client():
    tokens_file = f"{temp_dir()}/token.json"
    if not os.path.exists(tokens_file):
        msg = f"unable to generate credentials. tokens file not found at {tokens_file}"
        raise Exception(msg)

    creds = Credentials.from_authorized_user_file(tokens_file, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    if not creds.valid:
        raise Exception("credentials are not valid, provide new tokens.")

    with open(tokens_file, 'w') as token:
        token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service


def save_calendar_tokens():
    creds_file = f"{temp_dir()}/credentials.json"
    if not os.path.exists(creds_file):
        raise Exception(
            f"unable to generate tokens, creds file not found at {creds_file}")

    flow = InstalledAppFlow.from_client_secrets_file(
        f"{temp_dir()}/credentials.json", SCOPES,
    )
    creds = flow.run_local_server(port=0)
    tokens_file = f"{temp_dir()}/token.json"
    with open(f"{temp_dir()}/token.json", 'w') as token:
        token.write(creds.to_json())
    print(f"saved tokens to {tokens_file}")
