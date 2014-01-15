#-*- coding:UTF-8 -*-
'''
Created on 2013年12月27日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: find pattern 1 ****[value] attribute value

'''
from collections import Counter
category_entropy_file = open('D://xubo//ENwiki//sample//sample_entropy_produced.txt', 'r')
lines = category_entropy_file.readlines()
category_pattern_list = list()
for line in lines:
    line = line.rstrip()
    words = line.split("\t")
    category = words[0]
    attribute = words[1]
    value = words[2]
    if value in category:
        category_pattern = category.replace(value, '[value]')
        category_pattern_list.append((attribute, category_pattern))

c = Counter(category_pattern_list)
print c.most_common(10)
