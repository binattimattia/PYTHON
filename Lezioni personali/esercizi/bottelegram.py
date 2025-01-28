import requests
from plyer import notification
import schedule
import time
import random

# Token del tuo bot Telegram
BOT_TOKEN = "8137706958:AAHqPWxLpvciEHbQ_Ou0Xx-iR2QYI1dFTTU"
# Chat ID (il tuo chat ID, che hai ottenuto)
CHAT_ID = "1206447825"

# Funzione per inviare messaggio su Telegram usando requests
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

# Lista di messaggi motivazionali
messages = [
    "Ricordati di inserire la formazione al Fantacalcio ⚽!"
]

# Funzione per inviare la notifica desktop
def send_notification():
    # Scegli un messaggio casuale
    message = messages[0]
    # Notifica desktop
    notification.notify(
        title="Promemoria Motivazionale",
        message=message,
        timeout=10
    )
    # Notifica Telegram
    send_telegram_message(message)

# schedule.every().friday.at("17:30").do(send_notification)
schedule.every().minute.do(send_notification)

print("Il programma è in esecuzione.")

while True:
    schedule.run_pending()
    time.sleep(1)
