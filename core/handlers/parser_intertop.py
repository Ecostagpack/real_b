import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


async def get_card_link(session, page):
    useragent = UserAgent().random
    headers = {
        'User-Agent': useragent
    }
    url = f'https://intertop.ua/ua/deals/11345/?page={page}'
    with open('datas/old_data_link.json', 'r', encoding='utf-8') as file:
        old_data_link = json.load(file)

        async with session.get(url=url, headers=headers) as r:
            response_text = r.text()
            soup = BeautifulSoup(await response_text, 'lxml')
            items = soup.find_all('div', class_='one-product-in')
            data_card = []
            count = 0
            new_links = []
            for item in items:
                link = item.find('div', class_='product-thumb').find('a').get('href')


                if link not in old_data_link:

                    url = link
                    print(link)
                    try:
                        response2 = await session.get(url=url, headers=headers)
                        soup = BeautifulSoup(await response2.text(), 'lxml')
                        model = soup.find('h2', class_='user-product-name').find_all('div')[-1].text.strip()
                        # print(model)
                        brend = soup.find('h2', class_='user-product-name').find_all('div')[0].text.strip()
                        old_price = int(
                            soup.find('div', class_='pay-pr').find('span', class_='was-price').find('span').text.replace(
                                ' ',
                                '').strip())
                        action_price = int(
                            soup.find('div', class_='pay-pr').find('span', class_='now-price red-price').find(
                                'span').text.replace(' ', '').strip())
                        znizka = (old_price - action_price) / old_price * 100




                        if znizka > 25:
                            old_price = str(old_price) + 'грн'
                            action_price = str(action_price) + 'грн'
                            znizka = str(round(znizka)) + '%'


                            count += 1
                            print(f'Оброблено {count} карток')
                            # count += 1
                            # print(f'оброблено {count} карток')

                            data_card.append({'link': link,
                                              'Назва': model,
                                              'Бренд': brend,
                                              'Стара_ціна': old_price,
                                              'Акційна_ціна': action_price,
                                              'Знижка': znizka})


                    except Exception:
                        print('no conection to card')

                    new_links.append(link)
                    with open('datas/old_data_link.json', 'w', encoding='utf-8') as file:
                        json.dump(new_links, file, indent=4, ensure_ascii=False)
                    with open('datas/data_card.json', 'w', encoding='utf-8') as file:
                        json.dump(data_card, file, indent=4, ensure_ascii=False)

async def get_card_link_gather():
    useragent = UserAgent().random
    url = f'https://intertop.ua/ua/deals/11345/'
    headers = {
        'User-Agent': useragent
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        # soup = BeautifulSoup(await response.text(), 'lxml')
        tasks = []
        for page in range(1, 2):
            task = asyncio.create_task(get_card_link(session, page))
            tasks.append(task)
            print(f"[INFO] Обробив сторінку{page}")
        await asyncio.gather(*tasks)



def main():

    asyncio.run(get_card_link_gather())


if __name__ == '__main__':
    main()