#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
g_list = [11, 22, 33]


def work1(list):
    list.append(44)
    print("---in work1---", list)


def work2(list):
    # 延时一秒，保证线程t1中的事情做完
    time.sleep(1)
    print("---in work2---", list)


def main():
    # target指定这个线程去哪个函数执行代码
    # args指定调用函数时传递什么数据过去，args只接收元组
    t1 = threading.Thread(target=work1, args=(g_list,))
    t1.start()

    t2 = threading.Thread(target=work2, args=(g_list,))
    t2.start()


if __name__ == "__main__":
    main()