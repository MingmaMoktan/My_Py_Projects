import time
from plyer import notification

"""
Here is my drink water remainder app and here you need to install the package called plyer which will help you appear notification on your computer.
To install this package you can use the following command 
- pip install plyer

You can also use other similar kind of packages and have the similar functionality in the app. 

The app below will give you notification each and every hour.
"""

while True:
    notification.notify(title="Time to drink water",
                         message="Drink a glass of water.")
    time.sleep(60*60)