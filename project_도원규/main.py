#네이버 날씨에서 웹페이지 크롤링

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import time
from datetime import datetime
now = datetime.now()


def aircondition():
    # 네이버 날씨 URL
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    #pprint(html.text)

    soup = bs(html.text,'html.parser')

    address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
    print(address)

    #날씨 정보
    weather_data = soup.find('div',{'class':'weather_info'})

    #온도 정보
    temperature = weather_data.find('div',{'class':'temperature_text'}).text.strip()[5:]
    print(temperature)

    weather_status = weather_data.find('span',{'class':'weather before_slash'}).text
    print(weather_status)


    air = soup.find('ul',{'class':'today_chart_list'})
    infos = air.find_all('li', {'class':'item_today'})
    for info in infos:
        print(info.text.strip())

    # data1 = soup.find('div',{'class':'report_card_wrap'})
    # #pprint(data1)

    # data2 = data1.findAll('li')
    # #pprint(data2)

    # fine_dust1 = data2[0].find('strong',{'class':'title'}).text
    # fine_dust2 = data2[0].find('span',{'class':'txt'}).text
    # print(fine_dust1, fine_dust2)

    # ultra_fine_dust1 = data2[1].find('strong',{'class':'title'}).text
    # ultra_fine_dust2 = data2[1].find('span',{'class':'txt'}).text
    # print(ultra_fine_dust1, ultra_fine_dust2)

    # uv1 = data2[2].find('strong',{'class':'title'}).text
    # uv2 = data2[2].find('span',{'class':'txt'}).text
    # print(uv1,uv2)

if __name__=="__main__":

    while True:
        print("현재 : ", now.strftime('%Y-%m-%d %H:%M:%S'))
        aircondition()
        print("\n")
        time.sleep(10)
