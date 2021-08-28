from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Notifications!", "Hey how are u ? 😉😉", threaded=True, icon_path=None, duration=3)

# To chk if any notifications are active

import time
while toaster.notification_active():
    time.sleep(0.1)