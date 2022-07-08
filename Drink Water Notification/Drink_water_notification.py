# from socket import timeout
import time
from plyer import notification

if __name__ == "__main__" :

    # while True :
        title = '**** Drink Water Now ****'
        message= '''Getting enough water every day is important for your health.
Drinking water can prevent dehydration, a condition that can cause unclear thinking,
result in mood change, cause your body to overheat, and lead to constipation and kidney stones.'''
        notification.notify(title = title,
                        message = message,
                        app_icon = 'D:\Python Projects\Icon.ico',
                        timeout= 10,
                        toast = False)
        # time.sleep(60*60)