import pyautogui
import time
import keyboard

def autoclick(interval=1.0, playPause="="):
    print("Autoclick iniciado")
    running = False  

    while True:
        if keyboard.is_pressed("esc"):
            print("Programa encerrado")
            break

        if keyboard.is_pressed(playPause):
            running = not running
            print("Autoclick ON" if running else "Autoclick OFF")
            time.sleep(0.3)

        if running:
            pyautogui.click()
            time.sleep(interval)

def main():
    print("==========Autoclicker Simples==========")
    try:
        interval = float(input("Digite o intervalo entre cliques (em segundos, ex: 0.5): "))
        playPause = input("Digite a tecla para iniciar/parar o autoclick (padrão '='): ") or "="
    except ValueError:
        print("Valor inválido. Usando intervalo padrão de 1 segundo.")
        interval = 1.0
    input("Pressione Enter para iniciar o autoclick. Pressione Ctrl+C para parar.")
    autoclick(interval = interval, playPause=playPause)

main()