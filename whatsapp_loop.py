import pyautogui
import time
import webbrowser

phone_number = '+91123456789'  

webbrowser.open(f'https://web.whatsapp.com/send?phone={phone_number}')

time.sleep(10)

for i in range(1000):  
    message = "Write your message here in this string"
    pyautogui.typewrite(message)  
    pyautogui.press('enter')
    time.sleep(1)

