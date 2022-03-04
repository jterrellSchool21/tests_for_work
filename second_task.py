'''
Приведите код из синхронного вида к ассинхронному
'''

import asyncio
import time
import requests as r


def fetch_url_data(url):
    '''
    Получение ответа от источника
    '''
    try:
        resp = r.get(url)
    except Exception as e:
        print(e)
    else:
        return resp
    return


def fetch_async(r):
    '''
    Отправка запросов к источнику
    '''
    url = "https://www.cian.ru/cat.php?deal_type=rent&engine_version=2&offer_type=flat&p={}&region=1&room1=1&room2=1&type=4"
    tasks = []
    for i in range(r):
        tmp = url
        task = fetch_url_data(tmp.format(i))
        tasks.append(task)
    responses = tasks
    return responses


if __name__ == '__main__':
    '''
    Точка входа в программу
    '''
    for i in range(100):
        start_time = time.time()
        responses = fetch_async(i)
        print(f'Получено {i} результатов запроса за {time.time() - start_time} секунд')