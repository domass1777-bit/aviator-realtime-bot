import websocket
import json

historico = []

def on_message(ws, message):
    data = json.loads(message)
    mult = float(data.get("multiplier", 0))
    status = data.get("status", "")
    historico.append(mult)
    print(f"Multiplicador atual: {mult} | Status: {status}")

def on_error(ws, error):
    print("Erro:", error)

def on_close(ws):
    print("Conexão fechada")

def on_open(ws):
    print("Conexão aberta")

def iniciar_conexao(ws_url):
    ws = websocket.WebSocketApp(
        ws_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()
