#-*- coding:UTF-8 -*-
'''
Created on 2014年3月4日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
menu_path = "D://xubo//ENwiki//origin//"
result_path = menu_path + "all_infobox_statistic.txt"
result_file = open(result_path, 'r')

attribute_dict = dict()

lines = result_file.readlines()
print len(lines)

# for line in lines:
#     line = line.rstrip()
#     words = line.split("\t")
#     attribute = words[1]
#     exists = int(words[3])
#     if attribute not in attribute_dict:
#         attribute_dict[attribute] = list()
#     attribute_dict[attribute].append(exists)
# 
# attribute_file = open(menu_path + "attribute_statistic.txt", 'w')
# for k, v in attribute_dict.iteritems():
#     sum = 0
#     for v1 in v:
#         sum += v1
#     attribute_file.write("%s\t%s\t%s\n" % (k, str(sum), str(len(v))))