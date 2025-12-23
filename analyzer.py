def gerar_sinal(historico):
    if len(historico) < 5:
        return "AGUARDAR"

    ultimos = historico[-5:]
    baixos = [x for x in ultimos if x < 2.0]

    if len(baixos) >= 4:
        return "ENTRAR"
    return "AGUARDAR"
