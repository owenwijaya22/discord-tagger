import requests
import random
import json

# this function is for importing tokens from config.json
def choose_token():
    tokens = json.load('../config.json', 'r')["tokens"]
    token = random.choice(tokens)
    return token


def choose_url():
    subject = input('Math (m) or Physics (p): ')
    if subject == 'm':
        channels = random.choice([
            "536995777981972491", "754860723321962628", "641351291343208448",
            "917170713755017217", "803057978277888020", "704944645712642098"
        ])
        url = f"https://discord.com/api/v9/channels/{channels}/messages"
    elif subject == 'p':
        channels = random.choice(["627265780056195083", "536995799859724309"])
        url = f"https://discord.com/api/v9/channels/{channels}/messages"
    return url, channels


def main():
    url, channels = choose_url()
    token = choose_token()
    payload = "{\"content\":\"<@!300506208832585728> thank you\",\"nonce\":\"923027088506617856\",\"tts\":false}"
    headers = {'authorization': token, 'content-type': "application/json"}
    response = requests.post(url, data=payload,headers=headers).json()
    message_id = response['id']
    delete_url = f"https://discord.com/api/v9/channels/{channels}/messages/{message_id}"
    requests.delete(delete_url, headers=headers)


main()