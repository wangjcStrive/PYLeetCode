# -*- coding: utf-8 -*-
# @Time    : 5/14/2018 5:17 PM
# @FileName: temp.py
# Info: 

def func(aaa, bbb, *ccc):
    print(ccc)
    print(len(ccc))
    if len(ccc) == 1:
        print('len is 1')
        if len(ccc[0]) == len(aaa):
            print('ok')
        else:
            print('not ok')
    else:
        print('kkkkk')