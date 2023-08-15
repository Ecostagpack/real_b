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
diff_list = []


async def get_page_data(session, page):
    with open('datas/old_data_link.json', 'r', encoding='utf-8') as file:
        old_data_link = json.load(file)
    headers = {
        'User-Agent': useragent
    }
    url = f'https://intertop.ua/ua/deals/11345/?page={page}'

    async with session.get(url=url, headers=headers) as response:

        try:
            response_text = await response.text()

            soup = BeautifulSoup(response_text, 'lxml')
            items = soup.find_all('div', class_='one-product-in')
            for item in items:
                link = item.find('div', class_='product-thumb').find('a').get('href')
                new_data_link.append(link)
                if link not in old_data_link:
                    diff_list.append(link)
            # return new_data_link
            return diff_list
        except Exception:
            print('no conection')



async def gather_data():
    headers = {
        'User-Agent': useragent
    }
    url = f'https://intertop.ua/ua/deals/11345'

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')

        tasks = []
        for page in range(1, 2):
            task = asyncio.create_task(get_page_data(session, page))
            tasks.append(task)

        await asyncio.gather(*tasks)
        print(f"[INFO] Обробив сторінку{page}")

def main():
    asyncio.run(gather_data())
    curr_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    # with open('datas/old_data_link.json', 'w', encoding='utf-8') as file:
    #     json.dump(new_data_link, file, indent=4, ensure_ascii=False)

    with open('datas/diff_list.json', 'w', encoding='utf-8') as file:
        json.dump(diff_list, file, indent=4, ensure_ascii=False)

    finish_time = time.time()-start_time
    print(f"Витрачений на роботу час:{finish_time}")


if __name__ == '__main__':
    main()