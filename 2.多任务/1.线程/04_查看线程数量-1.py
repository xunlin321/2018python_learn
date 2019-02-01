#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time


def sing():
    for i in range(3):
        print("正在唱歌。。。%d" % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞。。。%d" % i)
        time.sleep(1)


if __name__ == "__main__":
    print("---开始---:%s" % time.ctime())  # ctime打印当前时间

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print("当前线程数为：%d" % length)
        if length <= 1:
            break

        time.sleep(1)