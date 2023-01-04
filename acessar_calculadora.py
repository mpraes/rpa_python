import pyautogui as auto

auto.sleep(2)
auto.moveTo(x=19, y=1061)
auto.click(x=19, y=1061)
auto.sleep(2)
auto.moveTo(x=148, y=791)
auto.click(x=148, y=791)
auto.sleep(1)
print(auto.position())