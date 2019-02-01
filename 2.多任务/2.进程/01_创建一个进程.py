#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import time

def run_proc():
    """子进程要执行的代码"""
    while True:
        print("---2---")
        time.sleep(1)



def main():
    p = multiprocessing.Process(target=run_proc)
    p.start()
    while True:
        print("---1---")
        time.sleep(1)


if __name__ == "__main__":
    main()