import MetaTrader5 as mt5
import time

mt5.initialize()

# pra obter os dados de uma empresa preicsa estar no mt5 tambem

simbolos = mt5.symbols.get()

print(simbolos)

len(simbolos) #Verificar quantos simbolos foram obtidos

simbolos[0].name

mt5.symbol_select("EDIE3")

preco_tempo_real = mt5.symbol_info("PETR4").last
retorno_tempo_real = mt5.symbol_info("PETR4").price_change

print(preco_tempo_real)


tempo = time.time() + 10 #horario/dia atual convertido em numeros

while time.time() < tempo:
    tick = mt5.symbol_info_tick("PETR4")
    print(f"o Fechamento é {tick.last}")
    print(f"o valor de compra é {tick.ask}")
    print(f"o valor de venda é {tick.bid}")
    print("------------------------------------")
    time.sleep(1)
