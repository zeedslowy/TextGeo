from twilio.rest import Client

# Twilio hesap bilgileri
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Twilio telefon numaraları
twilio_phone_number = 'your_twilio_phone_number'
recipient_phone_number = 'recipient_phone_number'

# Mesaj içeriği
message_body = 'Hello, this is a test message from Twilio!'

# Twilio client oluştur
client = Client(account_sid, auth_token)

# SMS gönderme işlemi
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=recipient_phone_number
)

# Gönderilen SMS bilgileri
print(f"Message sent with SID: {message.sid}")

