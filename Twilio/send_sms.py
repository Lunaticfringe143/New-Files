from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

client = TwilioRestClient(account_sid, auth_token)

my_message = " hey hi, how you doing Gandhi. It will good...please be patient"

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_message)