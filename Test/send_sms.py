from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC50a41c2e1a3f644b657f03477f812fb9"
# Your Auth Token from twilio.com/console
auth_token  = "8aeebe351de6354716626071039e3f56"

client = Client(account_sid, auth_token)
phone_number = 3016669240
phone_number = "whatsapp:+57" + str(phone_number)
message = client.messages.create(
    to= phone_number,
    from_="whatsapp:+14155238886",
    body="Es hora de tomar su medicina! Dirijase hacia la estación de medicamentos.")

print(message.sid)
