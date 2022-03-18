# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["AC9c3cac4f960dd9c95c501c72b48222f5"]
auth_token = os.environ["aa2d9e64ee9c4cd3b429c7a52d8ac6f7"]
client = Client(account_sid, auth_token)

phone_number = client.lookups.v1.phone_numbers("+15108675310").fetch(country_code="US")

print(phone_number.caller_name)
