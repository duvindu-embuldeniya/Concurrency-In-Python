import requests
from threading import Thread

class ImageDownloader(Thread):
    def __init__(self, thread_no, urls, queue):
        super(ImageDownloader, self).__init__()
        self.thread_no = thread_no
        self.urls = urls
        self.queue = queue
        self.success_count = 0
     
    
    def run(self):
        self.count = 0
        for url in self.urls:
            if self.download(self.thread_no, url,self.count ):
                self.success_count += 1
                self.count += 1
        self.queue.put(self.success_count)


    def download(self, thread_no, url, count):
        result = requests.get(url)
        if result.status_code == 200:
            with open(f'images/img{thread_no}-{count}.jpg', 'wb') as fw:
                fw.write(result.content)
                print(f"img{thread_no}-{count}.jpg downloaded successfully!!!")     
                return True
        
        else:
            print(f"img{thread_no}-{count}.jpg somethingwent wrong in downloading!!!")  
            return False   

