import pyautogui as auto

auto.sleep(2)


auto.moveTo(x=128, y=1059)
auto.click(x=128, y=1059)

auto.sleep(3)

auto.typewrite('https://www.google.com/')

auto.sleep(1)

auto.press('enter')

auto.sleep(1)

auto.typewrite('dolar hoje')

auto.sleep(1)

auto.press('enter')
