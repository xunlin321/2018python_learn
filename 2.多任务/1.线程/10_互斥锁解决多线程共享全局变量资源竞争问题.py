#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time

# 定义一个全局变量
g_num = 0
# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def test1(num):
    global g_num

    for i in range(num):
        # 上锁，如果之前没有被上锁，那么此时上锁成功
        # 如果上锁之前 已经上锁了，那么此时会堵塞在这里直到这个锁被解开为止
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("---in test1 g_num=%d---" % g_num)


def test2(num):
    global g_num

    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
    print("---in test2 g_num=%d---" % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待上面两个线程执行完毕。。。
    time.sleep(1)

    print("---in main Thread g_num=%d" % g_num)


if __name__ == "__main__":
    main()








