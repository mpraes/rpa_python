import pyautogui as auto

opcao = auto.confirm("Favor escolher qual programa deseja abrir: ", buttons = ['Chrome', 'Notepad++', 'Excel'])

def escolha_opcao(opcao):
    auto.hotkey('win', 'r')
    auto.sleep(2)
    if opcao == 'Chrome':
        auto.typewrite(opcao)
        auto.press('enter')
        auto.sleep(2)
    elif opcao == 'Notepad++':
        auto.typewrite(opcao)
        auto.sleep(1)
        auto.press('enter')
    elif opcao == 'Excel':
        auto.typewrite(opcao)
        auto.press('enter')
        auto.sleep(1)
        auto.press('enter')

escolha_opcao(opcao)
