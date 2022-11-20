from bs4 import BeautifulSoup
import fake_useragent
import requests
import random


user = fake_useragent.UserAgent().random
header = {'user-agent':user}
url_ex = 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=6&have=4'
url_Ancient_Orb_h = 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=518&have=4'
url_Ancient_Orb_ex = 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=518&have=6'


res = requests.get(url_ex,headers=header)
soup = BeautifulSoup(res.text,'lxml')
item = soup.find('div', class_='large-12 columns')
items = item.find_all('div', class_='displayoffer')
for num, ite in enumerate(items):
    if num > 3:
        ex_price = ite.find('div', class_='large-3 columns displayoffer-centered').text.strip()
        break

ex_price = ex_price[7:]
i = len(ex_price)
ex_price = float(ex_price[:i-2])

res = requests.get(url_Ancient_Orb_h,headers=header)
soup = BeautifulSoup(res.text,'lxml')
item = soup.find('div', class_='large-12 columns')
items = item.find_all('div', class_='displayoffer')
for num, ite in enumerate(items):
    if num > 7:
       price_h_Ancient_Orb = ite.find('div', class_='large-3 columns displayoffer-centered').text.strip()
       break
price_h_Ancient_Orb = price_h_Ancient_Orb[7:]
i = len(price_h_Ancient_Orb)
price_h_Ancient_Orb = float(price_h_Ancient_Orb[:i-2])


def main_function(Url_h, url_ex, name_van, name_final):
    res = requests.get(url_ex,headers=header)
    soup = BeautifulSoup(res.text,'lxml')
    item = soup.find('div', class_='large-12 columns')
    items = item.find_all('div', class_='displayoffer')
    items_pp = item.find_all('div', class_='large-3 columns displayoffer-centered')
    for num, ite in enumerate(items):
        if num > 7:
           price_ex_Ancient_Orb = ite.find('div', class_='large-3 columns displayoffer-centered').text.strip()
           for tik, _ite in enumerate(items_pp):
               if tik == 15:
                   price_amount_Ancient_Orb = _ite.text.strip()
                   break
    price_ex_Ancient_Orb = price_ex_Ancient_Orb[7:]
    i = len(price_ex_Ancient_Orb)
    price_ex_Ancient_Orb = float(price_ex_Ancient_Orb[:i-2])

    price_amount_Ancient_Orb = price_amount_Ancient_Orb[7:]
    i = len(price_amount_Ancient_Orb)
    price_amount_Ancient_Orb = float(price_amount_Ancient_Orb[:i-2])

    res = requests.get(Url_h, headers=header)
    soup = BeautifulSoup(res.text, 'lxml')
    item = soup.find('div', class_='large-12 columns')
    items = item.find_all('div', class_='displayoffer')
    for num, ite in enumerate(items):
        if num > 7:
            price_h_Ancient_Orb = ite.find('div', class_='large-3 columns displayoffer-centered').text.strip()
            break
    price_h_Ancient_Orb = price_h_Ancient_Orb[7:]
    i = len(price_h_Ancient_Orb)
    price_h_Ancient_Orb = float(price_h_Ancient_Orb[:i - 2])

    name_van = float("{0:.1f}".format((ex_price * price_ex_Ancient_Orb - price_h_Ancient_Orb)))
    name_final = float("{0:.1f}".format((ex_price * price_ex_Ancient_Orb - price_h_Ancient_Orb) * price_amount_Ancient_Orb))
    return name_van, name_final


price_van_Ancient_Orb, price_final_Ancient_Orb = main_function('https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=518&have=4','https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=518&have=6', 'price_van_Ancient_Orb', 'price_final_Ancient_Orb')

price_van_Gilded_Harbinger_Scarab, price_final_Gilded_Harbinger_Scarab = main_function('https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=734&have=4','https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=734&have=6', 'trec', 'trefdh' )

price_van_Polished_Harbinger_Scarab, price_final_Polished_Harbinger_Scarab = main_function('https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=746&have=4', 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=746&have=6','gfdg','gdfvdfg')

price_van_Gilded_Ambush_Scarab, price_final_Gilded_Ambush_Scarab = main_function('https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=728&have=4', 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=728&have=6', 'gfdgdv', 'cssec')

price_van_Gilded_Divination_Scarab, price_final_Gilded_Divination_Scarab = main_function('https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=732&have=4', 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=732&have=6', 'gdfgdfg', 'gvdfqqqqw')

price_van_Deafening_Essence_of_Contempt, price_final_Deafening_Essence_of_Contempt = main_function('https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=75&have=4', 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=75&have=6', "gfdgdfg", "qws")

price_van_Skittering_Delirium_Orb, price_final_Skittering_Delirium_Orb = main_function('https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=75-847&have=4', 'https://currency.poe.trade/search?league=Archnemesis&online=x&stock=&want=75-847&have=6', 'gdfgdfg', 'qwq')


price_info = {
    'van_Ancient_Orb':price_van_Ancient_Orb,
    'final_Ancient_Orb':price_final_Ancient_Orb,
    'van_Gilded_Harbinger_Scarab':price_van_Gilded_Harbinger_Scarab,
    'final_Gilded_Harbinger_Scarab':price_final_Gilded_Harbinger_Scarab,
    'van_Polished_Harbinger_Scarab': price_van_Polished_Harbinger_Scarab,
    'final_Polished_Harbinger_Scarab':price_final_Polished_Harbinger_Scarab,
    'van_Gilded_Ambush_Scarab':price_van_Gilded_Ambush_Scarab,
    'final_Gilded_Ambush_Scarab':price_final_Gilded_Ambush_Scarab,
    'van_Gilded_Divination_Scarab':price_van_Gilded_Divination_Scarab,
    'final_Gilded_Divination_Scarab':price_final_Gilded_Divination_Scarab,
    'van_Deafening_Essence_of_Contempt':price_van_Deafening_Essence_of_Contempt,
    'final_Deafening_Essence_of_Contempt':price_final_Deafening_Essence_of_Contempt,
    'van_Skittering_Delirium_Orb':price_van_Skittering_Delirium_Orb,
    'final_Skittering_Delirium_Orb':price_final_Skittering_Delirium_Orb,
}
print(price_info)

