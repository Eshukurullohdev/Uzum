# sms_utils.py
from twilio.rest import Client

# Twilio konfiguratsiyasi
TWILIO_SID = 'AC194c305d3f68bef614db6eebcab97f7d'
TWILIO_AUTH_TOKEN = '87d78fe9a6d05e6fb124434fdba9669a'
TWILIO_PHONE_NUMBER = '+998123456789'

def send_sms(phone_number, message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )
