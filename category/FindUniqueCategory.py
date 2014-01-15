#-*- coding:UTF-8 -*-
'''
Created on 2013年12月31日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: find unique value from uniquevalue results

songs produced by boi-1da    label    cash money    8    15    18

标准： 1,2列相等，2大于3列的90%
'''

entropy_file = open("D:\\xubo\\ENwiki\\sample\\sample_entropy_produced.txt", 'r')
entropy_lines = entropy_file.readlines()
for line in entropy_lines:
    line = line.rstrip()
    words = line.split("\t")
    word3 = int(words[3])
    word4 = int(words[4])
    word5 = int(words[5])
    if word3 > word4 * 0.9 and word4 > word5 * 0.9:
        print line