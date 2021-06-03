import pyautogui
screenWidth, screenHeight = pyautogui.size()  #Obter o tamanho do monitor principal.
currentMouseX, currentMouseY = pyautogui.position()  #Obter a posição XY do mouse.
pyautogui.moveTo(100, 150)  #Mover o mouse para as coordenadas XY.
pyautogui.click()  #Clicar com o mouse.
pyautogui.click(100, 200)  #Mover o mouse para as coordenadas XY e clicar nelas.
pyautogui.move(0, 10) #Mover o mouse 10 pixels para baixo de sua posição atual.
pyautogui.doubleClick() #Clicar duas vezes com o mouse.
pyautogui.moveTo(500, 400, duration=2, tween=pyautogui.easeInOutQuad) #Usar a função de interpolação/atenuação para mover o mouse por 2 segundos com pausa de um quarto de segundo entre cada tecla.
pyautogui.click() 
pyautogui.write('Ola, Mundo!', interval=0.1) 
pyautogui.press('esc')  #Pressionar a tecla Esc.
pyautogui.keyDown('shift')  #Pressionar a tecla Shift e segurá-la.
pyautogui.press(['left', 'left', 'left'])  #Pressionar a tecla de seta para a esquerda 4 vezes.
pyautogui.keyUp('shift')  #Soltar a tecla Shift.
pyautogui.hotkey('ctrl', 'c')  #Pressionar a combinação de teclas de atalho Ctrl-C.
pyautogui.press('down')
pyautogui.hotkey('ctrl', 'v')  #Pressionar a combinação de teclas de atalho Ctrl-C.
pyautogui.alert('Esta é a mensagem para Tela.')  #Mostrar uma caixa de alerta aparecer na tela e pausar o programa até clicar em OK.
