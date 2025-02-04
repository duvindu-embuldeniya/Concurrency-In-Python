# from queue import Queue         # related to multithreading
from multiprocessing import Queue # related to multiprocessing (uniformity)
import time
from engine import *

if __name__ == "__main__":

    start = time.time()
    url = 'https://picsum.photos/id/237/200/300'

    url_lst1 = []
    for i in range(100):
        url = f"https://picsum.photos/id/{i}/200/300"
        url_lst1.append(url)

    url_lst2 = []
    for i in range(0, len(url_lst1), 10):
        urls = url_lst1[i:i+10]
        url_lst2.append(urls)

    queue = Queue()
    thread_lst = []
    for index, urls in enumerate(url_lst2):
        thread = ImageDownloader(index, urls, queue)
        thread.start()
        thread_lst.append(thread)
    
    for thread in thread_lst:
        thread.join()
    
    total = 0
    while not(queue.empty()):
        total += queue.get()
    
    time_diff = time.time() - start
    print(f"No of {total} images downloaded within {time_diff} seconds!!!")
