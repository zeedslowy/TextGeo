import telebot
from twilio.rest import Client

# Telegram Bot token'ı
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'

# Twilio hesap bilgileri
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Telegram bot oluştur
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.from_user.id
    user_text = message.text

    # SMS gönderme işlemi
    send_sms(user_id, user_text)

def send_sms(user_id, text):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            to='+1XXXXXXXXXX',  # Alıcı telefon numarası
            from_=TWILIO_PHONE_NUMBER,
            body=text
        )
        bot.send_message(user_id, f'SMS gönderildi! SID: {message.sid}')
    except Exception as e:
        bot.send_message(user_id, f'SMS gönderme hatası: {str(e)}')

if __name__ == "__main__":
    bot.polling(none_stop=True)
