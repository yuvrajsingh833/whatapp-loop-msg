import pyautogui
import time
import webbrowser

phone_number = '+91123456789'  

webbrowser.open(f'https://web.whatsapp.com/send?phone={phone_number}')

time.sleep(10)

for i in range(1000):  
    message = "Bhosada Minister, Kaise ho aap?"
    pyautogui.typewrite(message)  
    pyautogui.press('enter')
    time.sleep(1)

