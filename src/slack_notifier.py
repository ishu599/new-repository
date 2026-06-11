import requests

def send_to_slack(webhook_url, message):

    payload = {
        "text": message
    }

    response = requests.post(
        webhook_url,
        json=payload
    )

    response.raise_for_status()