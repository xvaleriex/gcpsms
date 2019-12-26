# Download the helper library from https://www.twilio.com/docs/python/install
import twilio
import os
from twilio.rest import Client


def parse_timestamp4(request):
    request_json = request.get_json()
    if request_json and 'datetime' in request_json:
        timestamp = request_json['datetime']
    if request_json and 'name' in request_json:
        name = request_json['name']

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    api_key = os.environ['TWILIO_API_KEY']
    api_secret = os.environ['TWILIO_API_SECRET']
    client = Client(api_key, api_secret, account_sid)

    try:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body='Hello {}. New post just arrived! Timestamp is {}.\n'.format(name, timestamp),
            from_='+12015524516',
            to='+420774810359'
        )
    except twilio.rest.TwilioException as e:
        print(e)
    except Exception as e:
        return e