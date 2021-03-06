#-*- coding:UTF-8 -*-
'''
Created on 2013年12月31日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: find unique value from uniquevalue results

songs produced by boi-1da    label    cash money    8    15    18

标准： 1,2列相等，2大于3列的90%
'''
from operator import itemgetter

attribute_pattern_dict = dict()

entropy_file = open("D:\\xubo\\ENwiki\\origin\\all_entropy.txt", 'r')
entropy_lines = entropy_file.readlines()
for line in entropy_lines:
    line = line.rstrip()
    words = line.split("\t")
    word3 = int(words[3])
    word4 = int(words[4])
    word5 = int(words[5])
#     if word3 > word4 * 0.5 and word4 > word5 * 0.5:
#         if words[2] in words[0]:
#             pattern = words[0].replace(words[2], "jxulie")
# #             print words[1], pattern, words[2]
#             if (words[1],pattern) not in attribute_pattern_dict:
#                 attribute_pattern_dict[(words[1],pattern)] = set()
#             attribute_pattern_dict[(words[1],pattern)].add(words[2])
    if word3 > word4 * 0.9 and word4 > word5 * 0.9:
        if words[2] in words[0]:
            pattern = words[0].replace(words[2], "jxulie")
    #             print words[1], pattern, words[2]
            if (words[1],pattern) not in attribute_pattern_dict:
                attribute_pattern_dict[(words[1],pattern)] = set()
            attribute_pattern_dict[(words[1],pattern)].add(words[2])

for k, v in sorted(attribute_pattern_dict.iteritems(), key = itemgetter(0,1), reverse = False):
    if len(v) > 5:
        print k[0], "\t", k[1], "\t", len(v)