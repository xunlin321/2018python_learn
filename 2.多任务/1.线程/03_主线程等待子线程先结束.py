#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

def test():
    for i in range(5):
        print("---test1---%d---" % i)
        time.sleep(1)


if __name__ == "__main__":
    # 在调用Thread之前打印线程信息
    print(threading.enumerate())

    t = threading.Thread(target=test)

    # 在调用Thread之后打印线程信息
    print(threading.enumerate())

    t.start()

    # 在调用start之后打印线程信息
    print(threading.enumerate())