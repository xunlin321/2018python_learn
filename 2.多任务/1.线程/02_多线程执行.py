#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time


def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)  # 切记，target接收函数名不是接收函数
        t.start()  # 启动线程，即让线程开始执行