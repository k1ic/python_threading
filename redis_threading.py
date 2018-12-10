# -*- coding: utf-8 -*-
# Tested in python34
# 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
import redis
import threading

def redis_sadd(redis, key, i):
    start = i*5000
    end = (i+1)*5000
    v = start

    while(v < end):
        redis.sadd(key, v)
        v=v+1
        print(threading.currentThread().ident, threading.currentThread().name, r.scard(key))

r = redis.Redis(host='172.16.88.8', port=7001, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
k='ck_t_set_40w'

if __name__ == '__main__':
    threads = []
    for i in range(80):
        t = threading.Thread(target=redis_sadd, args=(r, k, i, ))
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        #join()的作用是，在子线程完成运行之前，阻塞父线程。
        t.join()
