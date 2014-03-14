#-*- coding:UTF-8 -*-
'''
Created on 2014年1月17日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: filter entropy

'''

attribute_pattern_dict = dict()

entropy_file = open("D:\\xubo\\ENwiki\\origin\\all_entropy.txt", 'r')
filter_entropy_file = open("D:\\xubo\\ENwiki\\origin\\all_filter_entropy.txt", 'w')
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
    if word3 == word4 and word4 > word5 * 0.9:
        filter_entropy_file.write(line + "\n")
filter_entropy_file.close()

