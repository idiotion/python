# -*- coding: utf-8 -*-

import os

def searchmyfile(dir,str):
    for i in os.listdir(dir):
        folder=os.path.join(dir,i)
        if os.path.isdir(folder):
            searchmyfile(folder, str)
        if str in os.path.split(folder)[1]:
            print('%s 匹配成功!' %(folder))

if __name__ == '__main__':
    searchmyfile('I:\DataGuru', 'pdf')