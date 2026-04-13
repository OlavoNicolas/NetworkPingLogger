import os 
import platform 
import datetime
import time

sistema = platform.system()
host = "8.8.8.8"
log_ping = "status_rede.txt"

def teste():
    if sistema == "Windows":
        comando = f"ping -n 2 {host}\n"
    else:
        comando = f"ping -c 2 {host}\n"
    
    resultado = os.system(comando)
    return resultado == 0

print("Iniciando monitoramento de rede...")
time.sleep(2.5)

with open(log_ping, "a") as log:
     horario_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
     Status = "Online" if teste() else "Offline"
     
     registro = f"Sistema: {sistema} | Data/Hora: {horario_atual} | Host: {host} -> {Status}\n"
     print(registro.strip())
     log.write(registro)

print("Teste concluído. Log salvo em", log_ping)