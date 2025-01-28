from plyer import notification
import schedule
import time

def send_notification():
    notification.notify(
        title="Promemoria quotidiano",
        message="Non dimenticare di dedicarti ai tuoi progetti oggi! 💻",
        timeout=10  # Durata della notifica in secondi
    )

# Pianifica la notifica ogni giorno alle 9:00
schedule.every().day.at("20:43").do(send_notification)

print("Il programma è in esecuzione. La notifica verrà inviata ogni giorno alle 20:43.")

while True:
    schedule.run_pending()
    time.sleep(1)