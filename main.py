import json
import requests
import time
from colorama import Fore, Back, Style
from win10toast import ToastNotifier
d = json.loads(open("config.json", "r").read())


def checkProduct(product):
    # Returns True when available, False when unavailable
    r = requests.get(product["URL"], headers={
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"})
    return not (product["notAvailable"] in str(r.content))


def notify(product):
    toast = ToastNotifier()
    toast.show_toast(
        "Availability checker",
        f"{product['Name']} is now available!!!",
        duration=20,
        threaded=True
    )


while True:
    # Loops through items
    for i in d["products"]:
        available = checkProduct(i)
        if available != i["lastAvailability"]:
            # Writes availability to config.json
            i["lastAvailability"] = available
            open("config.json", "w").write(json.dumps(d))
            if available and d["notification"]:
                # notifies user if item is available and hasn't been notified yet
                notify(i)
        # Prints availability
        print(
            f"{i['Name']} {(d['columnWidth']-len(i['Name']))*' '}--> {Fore.GREEN if (available and d['colors']) else ''}{Fore.RED if ((not available) and d['colors']) else ''}{'Available' if available else 'Unavailable'}{Style.RESET_ALL}")
    # Sleeps
    time.sleep(d["checkInterval"])
