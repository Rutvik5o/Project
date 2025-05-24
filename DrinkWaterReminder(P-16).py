import time
from plyer import notification

while True:

    print("Please Sip some water!")

    time.sleep(3600)
    notification.notify(title="Please drink some water",
                        message="You need to drink some water",)




