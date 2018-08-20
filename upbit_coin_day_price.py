## Upbit에 올라온 코인들의 day 마다 high price와 low price를 json 파일로 만들기


import pprint
import json
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

every_coin = {}
'''
def bitcoin():
    url = "https://api.upbit.com/v1/candles/days"
    querystring = {"market":"KRW-BTC","count":10}
    response = requests.request("GET", url, params=querystring)
    response = response.text
    btc_data = json.loads(response)

    btc_list = []
    with open("bitcoin_price.json",'w') as f:
        for btc in btc_data:
            btc_list.append({"name" : btc["market"],
            "day":btc["candle_date_time_kst"][:10],
                             "high_price":btc["high_price"],
                             "low_price": btc["low_price"]})

        json.dump(btc_list,f)


    #pprint.pprint(btc_data)
    pprint.pprint(btc_list)

bitcoin()
'''
######################################################################
def show_All_coin():
    global every_coin
    url = "https://api.upbit.com/v1/market/all"
    response = requests.request("GET", url)
    response = response.text
    data = json.loads(response)
    coin_list = []
#   upbit에 존재하는 모든 코인의 '한글명','영어명','마켓'
#   pprint.pprint(data)

    for i in data:
        coin_list.append(i['market'])
        every_coin[i['market']] = []
    return coin_list


def show_min_price_coin():
    global every_coin
    coin_list = show_All_coin()

    with open("coin_price.json","w") as f:

        for mk in coin_list:
            url = "https://api.upbit.com/v1/candles/days"
            querystring = {"market":mk,"count":4}
            response = requests.request("GET",url,params=querystring)
            response = response.text
            coin_data = json.loads(response)
            for coin in coin_data:
                every_coin[coin['market']].append({"day":coin["candle_date_time_kst"][:10],"high_price":coin["high_price"],"low_price":coin["low_price"],"change_rate":coin["change_rate"]})

        json.dump(every_coin,f, sort_keys=True, indent=4, separators=(',', ': '))

show_min_price_coin()
