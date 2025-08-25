import pyautogui
import time

def autoclick(interval=1.0):
    print("Autoclick iniciado")
    try:
        while True:
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoclick finalizado")

def main():
    print("Autoclicker Simples")
    try:
        interval = float(input("Digite o intervalo entre cliques (em segundos, ex: 0.5): "))
    except ValueError:
        print("Valor inválido. Usando intervalo padrão de 1 segundo.")
        interval = 1.0
    input("Pressione Enter para iniciar o autoclick. Pressione Ctrl+C para parar.")
    autoclick(interval)

main()