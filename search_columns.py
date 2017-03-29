#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:25:57 2017

@author: julio
"""
import urllib.request
from lxml import html
import requests

import os
cwd = os.getcwd()
file = 'file://'+cwd+'/myfile5.html'

#import codecs
#f = codecs.open('myfile5.html', 'r', 'utf-8')

myfile5 = urllib.request.urlopen(file).read()
#page = requests.get('myfile5.html')
tree = html.fromstring(myfile5)


data = tree.xpath('(.|.//*[not(name()="script")][not(name()="style")])/text()')
len(data)

data_correct=data[0:-1]
while '\n' in data_correct: data_correct.remove('\n')   

count = -1
for n in data_correct:
    count += 1
    print(count)
    if '\n' in n:
        data_correct[count] = n[:-1]
    elif '\n' not in n:
        data_correct[count] = n+data_correct[count+1]
        #data_correct.append(n + data[data.index(n)+1])
        del data_correct[count+1]
        
 