from twilio.twiml.voice_response import Gather, VoiceResponse

# Twilio hesap bilgileri
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Twilio telefon numaraları
twilio_phone_number = 'your_twilio_phone_number'
recipient_phone_number = 'recipient_phone_number'

def generate_twiml():
    response = VoiceResponse()
    response.say("Hello! This is a Twilio voice call.")
    response.gather(numDigits=1, action='/handle-key', method='POST')
    return str(response)

# Çağrı almak için Flask kullanabilirsiniz (bu sadece örnek bir web framework'tür)
from flask import Flask, request

app = Flask(__name__)

@app.route('/answer', methods=['GET', 'POST'])
def answer_call():
    twiml_response = generate_twiml()
    return twiml_response, 200, {'Content-Type': 'application/xml'}

@app.route('/handle-key', methods=['POST'])
def handle_key():
    digit_pressed = request.values['Digits']
    # Handle the digit pressed (this is just an example)
    print(f"Digit pressed: {digit_pressed}")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
