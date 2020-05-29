import requests

# Get API Token
oauthtask = {"response_type": "code", "client_id": "a15b0252-1b04-4502-8bce-b382318b0f6c", "scope": "read"}
oauthresp = requests.get('developer.blackboard.com/learn/api/public/v1/oauth2/authorizationcode', json=oauthtask)
if oauthresp.status_code != 200:
    print('Error {}'.format(oauthresp.status_code))
print('Created task. ID: {}'.format(oauthresp.json()["id"]))