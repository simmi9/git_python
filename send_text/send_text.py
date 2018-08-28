import twilio
import twilio.rest
from twilio.rest import Client
#your account sid and auth token from twilio.com/user/account

account_sid= "ACa56edcc24ad71ec70d155f*********"
auth_token = "eb8b28681edb4ca***************"
client = Client(account_sid , auth_token)

message = client.messages.create(
    body = "My name is Bhawna",
    to = "+16*********", #twilio phone number
    from_ = "3068024328 " ) #your phone number
print (message.sid)
