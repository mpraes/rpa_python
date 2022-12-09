import pyautogui as auto

def abrir_Excel():
    auto.sleep(1)
    auto.moveTo(x=33, y=1051)
    auto.click(x=33, y=1051)
    auto.sleep(2)
    auto.typewrite('Excel')
    auto.sleep(4)
    #auto.click(x=33, y=1051)
    #print(auto.position())
    auto.moveTo(x=186, y=250)
    auto.click(x=186, y=250)
    auto.sleep(3)
    print(auto.position())
    auto.moveTo(x=446, y=289)
    auto.click(x=446, y=289)
    auto.sleep(2)
    print(auto.position())
    auto.moveTo(x=78, y=392)
    auto.click(x=78, y=392)

abrir_Excel()