import pyautogui as pa
import time

pa.PAUSE = 2

print("Você tem 5 segundos para posicionar a página...")
time.sleep(5)

# Mostra a posição atual do mouse
print("Posição:", pa.position())

# # Clica no EXCLUIR do contato
# pa.click(x=-430, y=616)

# time.sleep(2)

# # Clica no EXCLUIR dentro do modal
# pa.click(x=-992, y=389)

# time.sleep(10)

# print("Teste concluído.")