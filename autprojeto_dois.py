import pyautogui, keyboard
from time import sleep

"Para este projeto vamos criar um bot para zerar o game Guitar Flash (https://guitarflash.com/)"

"OBS: Para este projeto, é necessário instalar a biblioteca keyboard (pip install keyboard - no cmd)"


# Vamos captar as cores dos botões do game. Fazemos isso da seguinte forma:
# Damos um "print" na tela, colocamos a imagem no paint, e retiramos a cor da tela usando o parametro f5 no mouseInfo


# Abaixo: Enquanto não pressionamos a tecla 1, o codigo continuará
while keyboard.is_pressed('1') == False:  
    # Aqui estamos pegando a coordenada do ponto de acerto (quando devemos apertar o botão) e a cor do botão (neste caso o verde)
    if pyautogui.pixelMatchesColor(1246,817,(0,152,0)):
        pyautogui.press('a')
        sleep(0.01)  # 0.1 segundo

    if pyautogui.pixelMatchesColor(1357,815,(255,0,0)):  # vermelho
        pyautogui.press('s')
        sleep(0.01)

    if pyautogui.pixelMatchesColor(1472,817,(244,244,2)):  # amarelo
        pyautogui.press('j')
        sleep(0.01)

    if pyautogui.pixelMatchesColor(1582,818,(0,152,255)):  # azul
        pyautogui.press('k')
        sleep(0.01)

    if pyautogui.pixelMatchesColor(1695,818, (255,101,0)):  # laranja
        pyautogui.press('l')
        sleep(0.01)

# pixelMatchesColor ->  verifica a cor de um pixel