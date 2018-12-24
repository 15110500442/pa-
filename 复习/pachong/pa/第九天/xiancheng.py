import threading
import time

def download(url):
    print(url)
    time.sleep(2)
    print(threading.current_thread().name)
    #睡眠1秒




def main():
    starttime = time.time()
    task = ['url1','url2','url3','url4']
    # for url in task:
    #     download(url)
    for url in task:
        t = threading.Thread(target=download,name='xiancheng'+url,args=(url,))
        t.setDaemon(True)
        t.start()
    endtime = time.time()
    print('耗时'+str(endtime-starttime))


if __name__ == '__main__':
    main()