import datetime
import json
import requests
from bs4 import BeautifulSoup
import lxml
# import jsondiff
import time
from fake_useragent import UserAgent
import aiohttp
import asyncio

useragent = UserAgent().random
start_time = time.time()
new_data_link = []
# diff_list = []
data_card = []


# async def get_data_card(session, url):
#     async with session.get(url) as resa:
#         return await resa.text()
#
#
# async def get_data_card_gather(session, urls):
#     tasks = []
#     for url in urls:
#         task = asyncio.create_task(get_data_card(session, url))
#         tasks.append(task)
#     results = await asyncio.gather(*tasks)
#     return results
#
#
# async def main(urls):
#     async with aiohttp.ClientSession() as session:
#         data = await get_data_card_gather(session, urls)
#         return data
#
#
# def parse(results):
#     count = 0
#     data_card = []
#     for target in results:
#         soup = BeautifulSoup(target, 'lxml')
#         link = url
#         model = soup.find('h2', class_='user-product-name').find_all('div')[-1].text.strip()
#         brend = soup.find('h2', class_='user-product-name').find_all('div')[0].text.strip()
#         old_price = int(soup.find('div', class_='pay-pr').find('span', class_='was-price').find('span').text.replace(' ', '').strip())
#         action_price = int(soup.find('div', class_='pay-pr').find('span', class_='now-price red-price').find('span').text.replace(' ', '').strip())
#         znizka = (old_price - action_price) / old_price * 100
#
#         if znizka > 25:
#             old_price = str(old_price) + 'грн'
#             action_price = str(action_price) + 'грн'
#             znizka = str(round(znizka)) + '%'
#
#             count += 1
#             print(f'оброблено {count} карток')
#
#             data_card.append({'link': link,
#                               'Назва': model,
#                               'Бренд': brend,
#                               'Стара_ціна': old_price,
#                               'Акційна_ціна': action_price,
#                               'Знижка': znizka})
#         # print(data_card)
#
#
# if __name__ == '__main__':
#     with open('datas/diff_list.json', 'r', encoding='utf-8') as file:
#         links_list = json.load(file)
#     with open('datas/data_card.json', 'w', encoding='utf-8') as file:
#         json.dump(data_card, file, indent=4, ensure_ascii=False)
#         urls = links_list
#         results = asyncio.run(main(urls))
#         parse(results)
#         curr_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
#         finish_time = time.time() - start_time
#         print(f"Витрачений на роботу час:{finish_time}")

# ************************************************************************************
def get_data_card():
    with open('datas/diff_list.json', 'r', encoding='utf-8') as file:
        diff_list = json.load(file)

        data_card = []
        count = 0
        for url2 in diff_list:
            headers = {
                'User-Agent': useragent
            }
            try:
                response = requests.get(url=url2)
                soup = BeautifulSoup(response.text, 'lxml')
                link = url2
                model = soup.find('h2', class_='user-product-name').find_all('div')[-1].text.strip()
                brend = soup.find('h2', class_='user-product-name').find_all('div')[0].text.strip()
                old_price = int(
                    soup.find('div', class_='pay-pr').find('span', class_='was-price').find('span').text.replace(' ',
                                                                                                                 '').strip())
                action_price = int(soup.find('div', class_='pay-pr').find('span', class_='now-price red-price').find(
                    'span').text.replace(' ', '').strip())
                znizka = (old_price - action_price) / old_price * 100

                if znizka > 25:
                    old_price = str(old_price) + 'грн'
                    action_price = str(action_price) + 'грн'
                    znizka = str(round(znizka)) + '%'

                    count += 1
                    print(f'оброблено {count} карток')
#
                    data_card.append({'link': link,
                                      'Назва': model,
                                      'Бренд': brend,
                                      'Стара_ціна': old_price,
                                      'Акційна_ціна': action_price,
                                      'Знижка': znizka})
            except Exception:

                print('no conection to card')

        with open('datas/data_card.json', 'w', encoding='utf-8') as file:
            json.dump(data_card, file, indent=4, ensure_ascii=False)

get_data_card()


# def rewrite_old_data_link():
#     with open('datas/new_data_link.json', 'r', encoding='utf-8') as file:
#         new_data_link = json.load(file)
#
#     with open('datas/old_data_link.json', 'w', encoding='utf-8') as file:
#         json.dump(new_data_link, file, indent=4, ensure_ascii=False)
#
# rewrite_old_data_link()