import requests
import json
from bs4 import BeautifulSoup


def JPYKRW():
    url = 'https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_JPYKRW_SHB'
    req = requests.get(url)

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    rateList = soup.select(
        "#content > div.spot > div.today > p.no_today > em > em"
    )

    strRate = ""
    for item in rateList:
        strRate = strRate + str(item.text)

    strRate = strRate.replace('\n', '')
    strRate = strRate.replace(',', '')
    rate = float(strRate)

    return rate


def XRPJPY():
    url = "https://public.bitbank.cc/xrp_jpy/ticker"
    res = requests.get(url)

    resData = res.json()["data"]
    # print(resData)

    nowXrp = float(resData['last'])
    nowTime = resData['timestamp']

    return nowXrp


def XRPKRW():
    url = "https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw"
    res = requests.get(url)

    resData = res.json()
    # print(resData)

    nowXrp = float(resData['last'])
    nowTime = resData['timestamp']

    return nowXrp

# print(JPYKRW())
# print(XRPKRW())
# print(XRPJPY())