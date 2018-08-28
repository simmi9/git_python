import twilio
import twilio.rest
from twilio.rest import Client
#your account sid and auth token from twilio.com/user/account

account_sid= "ACa56edcc24ad71ec70d155f0fb016171f"
auth_token = "eb8b28681edb4ca63519c2b9296905fc"
client = Client(account_sid , auth_token)

message = client.messages.create(
    body = "My name is Bhawna",
    to = "+16473282741", #twilio phone number
    from_ = "3068024328 " ) #your phone number
print (message.sid)
