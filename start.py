import requests
import json

# Get API Token
def auth_code():
    oauthtask = {"response_type": "code", "client_id": "", "scope": "read"}
    oauthresp = requests.get('developer.blackboard.com/learn/api/public/v1/oauth2/authorizationcode', json=oauthtask)
    if oauthresp.status_code != 200:
        print('Error {}'.format(oauthresp.status_code))
    print('Created task. ID: {}'.format(oauthresp.json()["id"]))