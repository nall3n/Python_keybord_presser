


import time
import datetime
import pyautogui

isrunning = True
run_time = datetime.datetime(2024,2,27,9,10,0)
delta_time = datetime.timedelta(minutes=1)


def press_button():
    pyautogui.press('1')
    pyautogui.press('enter')


while isrunning: 
    if datetime.datetime.now() >= run_time:
        press_button()
        run_time += delta_time
        print(run_time)
