import pyautogui
import time

'''
# Aguarda por 5 segundos antes de iniciar o loop
time.sleep(5)

# Coordenadas desejadas para os cliques | My screen
coordenadas = [
    (1090, 423),
    (765, 444),
    (1075, 413)
]

while True:
    for x, y in coordenadas:
        # Clica na coordenada específica
        pyautogui.click(x, y)

        # Aguarda por 2 segundos entre os cliques
        time.sleep(2)
'''

# Aguarda por 5 segundos antes de iniciar o loop
time.sleep(5)

# Coordenada desejada para o clique
coordenadas = (1265, 1098)

while True:
    # Clica na coordenada específica
    pyautogui.click(coordenadas)

    # Aguarda por 2 segundos entre os cliques
    time.sleep(2)
