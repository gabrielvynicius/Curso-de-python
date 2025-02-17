import time

def relogio():
    while True:
        agora = time.localtime()
        hora_atual = time.strftime("%H:%M:%S", agora)
        print(hora_atual, end="\r")
        time.sleep(1)

if __name__ == "__main__":
    relogio()