import pyautogui as pg
import time


serie_1 =range(1, 11)

listas =list(serie_1)

lista_numeros =list(map(lambda numero : numero**2, listas))

print(lista_numeros)

# Tiempo entre clics (en segundos)
intervalo = 50 


time.sleep(3)  

while True:
    pg.click()  
    print("Clic realizado.")
    time.sleep(intervalo)


