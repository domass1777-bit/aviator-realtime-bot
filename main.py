from websocket_reader import iniciar_conexao, historico
from analyzer import gerar_sinal
from bankroll import calcular_aposta

banca = 100.0

ws_url = "wss://URL_DO_WEBSOCKET_DO_AVIATOR"  # colocar URL real

# Inicia conexão WebSocket em background
import threading
t = threading.Thread(target=iniciar_conexao, args=(ws_url,))
t.start()

# Loop principal do bot
import time
while True:
    if len(historico) >= 5:
        sinal = gerar_sinal(historico)
        if sinal == "ENTRAR":
            aposta = calcular_aposta(banca)
            print(f"⚡ SINAL: ENTRAR | Apostando: {aposta}")
        else:
            print("⏸️ AGUARDANDO")
    time.sleep(1)
