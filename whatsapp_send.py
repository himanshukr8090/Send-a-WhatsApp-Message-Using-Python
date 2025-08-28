import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twilio credentials from .env
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_whatsapp = "whatsapp:+14155238886"   # Twilio Sandbox WhatsApp number
to_whatsapp = "whatsapp:+91XXXXXXXXXX"     # Replace with your WhatsApp number

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! 🚀 This is an automated WhatsApp message from Python.",
    from_=twilio_whatsapp,
    to=to_whatsapp
)

print(f"WhatsApp message sent successfully! SID: {message.sid}")

