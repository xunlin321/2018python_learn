#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time

g_num = 100


def work1():
    global g_num
    for i in range(100):
        g_num += 1

    print("---in work1,g_num is %d---" % g_num)


def work2():
    global g_num
    print("---in work2,g_num is %d---" % g_num)


def main():
    print("---线程创建之前的g_num is %d---" % g_num)

    t1 = threading.Thread(target=work1)
    t1.start()

    # 延时一秒保证线程t1中的事情做完
    time.sleep(1)

    t2 = threading.Thread(target=work2)
    t2.start()


if __name__ == "__main__":
    main()