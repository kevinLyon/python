import json

import websocket


def ao_abrir(ws):
    print('Conexão aceita!')
    
    js_scrib = """{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
    }"""
    try:
        ws.send(js_scrib)
    except Exception as erro:
        print('Erro ao enviar js_scrib')
        print(erro)


def erro(ws, error):
    print(error)


def menssagem(ws, message):
    raw = message
    parsing = json.loads(raw)
    print(r'Bitcoin em tempo real {btc_USD}: $', parsing['data']['price'])


def ao_fechar(ws):
    print('### Closed ###')


if __name__ == "__main__":
    ws = websocket.WebSocketApp( "wss://ws.bitstamp.net", on_open=ao_abrir, on_close=ao_fechar, on_message=menssagem, on_error=erro)

    ws.run_forever()