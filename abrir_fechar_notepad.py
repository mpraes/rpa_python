#Neste script eu consigo acessar o notepad via teclas, escrever algo e sair sem salvar

import pyautogui as auto

auto.hotkey('win', 'r')
auto.sleep(2)

auto.typewrite('notepad')
auto.press('enter')
auto.sleep(2)

auto.typewrite('Este é um script escrevendo sozinho')
fechar = auto.getActiveWindow()
fechar.close()
auto.sleep(1)

auto.press('tab')

auto.press('enter')
