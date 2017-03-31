#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:25:57 2017

@author: julio
"""
import urllib.request
from lxml import html
#import requests
import re
#from parse import *
#from urllib.parse import urlparse
#from urllib.parse import search

import os
cwd = os.getcwd()
file = 'file://'+cwd+'/myfile5.html'


myfile5 = urllib.request.urlopen(file).read()
myfile5 = myfile5.decode("utf-8") 

tree = html.fromstring(myfile5)
data = tree.xpath('(.|.//*[not(name()="script")][not(name()="style")])/text()')

data_correct=data[0:-1]
for i,n in enumerate(data_correct):
    if '\n' not in n:    
        data_correct[i] = data_correct[i] + ' ' + data_correct[i+1]
        #data_correct.append(n + data[data.index(n)+1])
        del data_correct[i+1]
while '\n' in data_correct: data_correct.remove('\n')   

for i,n in enumerate(data_correct):
    data_correct[i] = data_correct[i].strip()


#%% Find attributes
top = re.findall("div style.*top:([0-9]+)px.", myfile5)
left = re.findall("div style.*left:([0-9]+)px.", myfile5)
titles = []
for i,n in enumerate(data_correct): 
    #if (re.findall("([A-Z]{2,}) ([0-9]*)?", data_correct[i])):
     #if (re.findall("(^[A-Z]{2,}).* ([A-Z]{2,})", data_correct[i])):
    mo = re.search("(([A-Z]{2,}( [0-9]+)*(.*%)*)(.*[A-Z]+)*)", titles[0]) #works for titles[0]
        titles.append(n)
        
        
       # if (re.findall("$[A-Z]{2,}", titles[n])):
           # titles[n].split
#top.group() ([0-9]+).*: (.*) ([A-Z]{2,})*
