#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading


def test1():
    for i in range(3):
        print("---test1---%d---" % i)
        time.sleep(1)


def test2():
    for i in range(6):
        print("---test2---%d---" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        time.sleep(1)
        if len(threading.enumerate()) <= 1:
            break


if __name__ == "__main__":
    main()

