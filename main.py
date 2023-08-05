from pix2tex.cli import LatexOCR
import subprocess
import pyautogui as pt
import pyperclip
from pynput import keyboard as ks
from sys import platform
from windows_toasts import WindowsToaster, ToastText1


def send_notification_windows(title="title"):
    wintoaster = WindowsToaster("OCR")
    newToast = ToastText1()
    newToast.SetBody(title)
    wintoaster.show_toast(newToast)



def send_notification_linux(title="", description=""):
    os.system('notify-send "{}" "{}"'.format(title, description))


send_notification = None
if platform.startswith("win"):
    send_notification = send_notification_windows
if platform == "linux":
    send_notification = send_notification_linux
# icon directory

# The key combination to check
COMBINATION = {ks.Key.ctrl_l, ks.Key.alt_l, ks.Key.shift_l}

# Globals
current = set()
screenshot_mode = False
start_x = 0
start_y = 0


def on_press(key):
    global start_x, start_y, screenshot_mode
    try:
        if key in COMBINATION:
            current.add(key)

            if screenshot_mode:
                end_x, end_y = pt.position()
                im = pt.screenshot(region=(start_x, start_y, end_x - start_x, end_y - start_y))

                # img = Image.open('example.png')
                model = LatexOCR()
                txt = model(im)
                txt = '$' + txt + '$'
                print(txt)

                pyperclip.copy(txt)

                send_notification("Copied to Clipboard!")

                screenshot_mode = False
                current.clear()

            # on first press
            if all(k in current for k in COMBINATION) and not screenshot_mode:
                send_notification("Entered Screenshot Mode")
                start_x, start_y = pt.position()
                screenshot_mode = True
                current.clear()

    except Exception as e:
        screenshot_mode = False
        current.clear()

        send_notification("Error: " + str(e))

    if key == ks.Key.esc and screenshot_mode:
        screenshot_mode = False
        current.clear()
        send_notification("Exited Screenshot Mode")


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with ks.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
