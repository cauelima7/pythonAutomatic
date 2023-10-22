import pyautogui as py
import random
import time

def automatico(mensagens, velocidade):
    time.sleep(5)

    for i in range(velocidade):
        msg = random.choice(mensagens)
        py.write(msg)
        py.press("enter")