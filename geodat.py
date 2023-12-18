from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Twilio hesap bilgileri
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-sms', methods=['POST'])
def send_sms():
    recipient_number = request.form['recipient_number']
    message_body = request.form['message_body']

    # Twilio'ya SMS gönderme
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=recipient_number,
        from_=TWILIO_PHONE_NUMBER,
        body=message_body
    )

    return f'SMS sent! SID: {message.sid}'

if __name__ == '__main__':
    app.run(debug=True)
