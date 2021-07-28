import pyautogui as auto
from time import sleep

print('Enter what you want to spam:')
k = input()

while True:
    auto.write(k)
    auto.press('enter')
    sleep(1)