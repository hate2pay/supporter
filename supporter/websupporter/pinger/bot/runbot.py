import sh
import threading
import time

HOSTS = ['ya.ru', 'yandex.ru', 'google.com', 'ostro.org']
HOSTS2 = ['ya1.ru', 'ssh.ru', 'vk.com', 'os15.org']
def pinghost(hosts):
    while True:
        for host in hosts:
            try:
                sh.ping('-c', '2', host)
            except:
                print(host + ' is DOWN!')
            else:
                print(host + ' is UP!')
        return None

p1 = threading.Thread(target=pinghost, name='t1', args=[HOSTS])
p2 = threading.Thread(target=pinghost, name='t2', args=[HOSTS2])
p1.start()
p2.start()
'''    while not threading.activeCount() == 1:
        time.sleep(1)
    print(threading.activeCount())'''
