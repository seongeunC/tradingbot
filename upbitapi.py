import requests
import sys
import io
import pprint
import json

#script 한글 출력
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def show_All_coin():
    url = "https://api.upbit.com/v1/market/all"
    response = requests.request("GET", url)
    response = response.text
    data = json.loads(response)
    coin_list = []
#   upbit에 존재하는 모든 코인의 '한글명','영어명','마켓'
#   pprint.pprint(data)
    for i in data:
        coin_list.append(i['market'])

    return coin_list

def show_min_price_coin():
    coin_list = show_All_coin()
    url = "https://api.upbit.com/v1/candles/minutes/1"
    min_coin_info = []
    with open("min_coin_info.txt","a") as f:
        for mk in coin_list:
            querystring = {"market":mk}
            response = requests.request("GET",url,params=querystring)
            response = response.text
            f.write(response)
            data = json.loads(response)
            min_coin_info.append(data)



        f.close()

    return pprint.pprint(min_coin_info)



show_min_price_coin()
