import config
from binance.client import client
from binance.enums import *
import time
import datetime
import numpy as np

# From here we start to write the code...

cliente = Cliente(config.API_KEY, config.onfig.API_SECRET, tld='com')
symbolTicker = 'BTCUSD'
quantityOrders = 0.0013


def tendencia():
    x = []
    y = []
    sum = 0
    ma50_i = 0

    reso = False

    klines = client.get_historical_klines[symbolTicker, Client.KLINE_INTERNAL_15MINUTE, "18 hour ago UTC"]

    if (len(klines))



# Vamos hacer una funcion de la media de 50 
# agarra las 50 velas anteriores, tomar los precios de cierre de las 50 velas sumarlos y dividirlos por 50

def _ma50_():
    kilines = client.get_historical_klines(symbolTicker, Client.KLINE_INTERNAL_15MINUTE, "15 hour ago GMT")


    if (len(kilines)==60):
        for i in range (10,60):
            sum = sum + klines[i][4]
            na50_local = sun / 50


    return ma50_local



while 1:

    orders = client.get_open_orders(symbol=symbolTcicker)

    if (len(orders) i= 0):
        print(*THERE IS OPEN ORDERS*)
        time.sleep(10)
        continue



        #To get price
    list_of_tickers = client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tcik_2['symbol'] == symbolTicker:
            symbolPrice = float(tick_2['price'])

        #get price

    
    ma50 = _ma50_()
    if (ma50 == 0): continue


    print("***** " + symbolTicker + " *******")
    print("ACTUAL MA50 " + round(ma50,2))
    print("Actual Price " + str(round(symbolPrice,2)))
    print("Price to Buy " + str(round(ma50*0.995,2)))




          

