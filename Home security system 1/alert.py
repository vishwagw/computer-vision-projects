# using twilio API
from twilio.rest import Client

client = Client("ACCOUNT_SID", "AUTH_TOKEN")
message = client.messages.create(
    to="+1234567890",
    from_="+0987654321",
    body="Suspicious activity detected!"
)

