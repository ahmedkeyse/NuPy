from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9c3cac4f960dd9c95c501c72b48222f5"
# Your Auth Token from twilio.com/console
auth_token = "aa2d9e64ee9c4cd3b429c7a52d8ac6f7"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16128072445", from_="+15017250604", body="Hello from Python!"
)

print(message.sid)
