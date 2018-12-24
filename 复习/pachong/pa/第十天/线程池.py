# 使用python3.2之后给我们封装的线程池
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import requests


def get_data(url):
    print('开始下载' + url)
    time.sleep(2)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    # print(response.status_code)
    if response.status_code == 200:
        return response.status_code, url


def done(future):
    # 线程池执行设定任务结束后的结果参数
    print('下载完了')
    response = future.result()
    print(response)


def main():
    # 定义一个线程池(池里面有三个创建好的线程,可以同时使用)
    # max_workers:这个参数意思是  同时能执行的最大的线程数
    pool = ThreadPoolExecutor(8)
    # 提交任务给线程
    urls = [
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
    ]
    for url in urls:
        # submit:表示将我们要执行的任务交个这个线程池
        handler = pool.submit(get_data, url)
        # 给线程池设置发任务之后，可以设置一个回掉函数，作用是：当我们某个任务执行完毕之后，就会回调你设置的回调函数
        # handler.add_done_callback()
        handler.add_done_callback(done)

    pool.shutdown(True)

    # 如何设置才能让主线程等待子线程任务结束后再结束
    print(threading.current_thread().name)


if __name__ == '__main__':
    main()
