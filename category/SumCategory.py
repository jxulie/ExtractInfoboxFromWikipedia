#-*- coding:UTF-8 -*-
'''
Created on 2013年12月27日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: sum +1 and -1

'''
from operator import itemgetter
from collections import Counter
menu_path = "D://xubo//ENwiki//refine//"
super_category_file = open(menu_path + "supercategory.txt", 'r')
lines = super_category_file.readlines()
category_dict = dict()
for line in lines:
    try:
        line = line.lower().rstrip()
        words = line.split("\t")
        category_dict[words[0]] = list()
        for i in range(1,len(words)):
            category_dict[words[0]].append(words[i])
    except:
        print "error : ", line
# 
#     line = line.rstrip()
#     words = line.split("\t")
#     category_dict[words[0]] = list()
#     for i in range(1,len(words)):
#         category_dict[words[0]].append(words[i])
super_category_file.close()


category_entropy_dict = dict()
category_entropy_file = open(menu_path + "filter_category_relation.txt", 'r')
category_entropy_lines = category_entropy_file.readlines()
for line in category_entropy_lines:
    line = line.rstrip()
    words = line.split("\t")
    category = words[0]
    attribute = words[1]
    value = words[2]
    if attribute not in category_entropy_dict:
        category_entropy_dict[attribute] = list()
    category_entropy_dict[attribute].append((category, value))
category_entropy_file.close()

print len(category_entropy_dict)

super_file = open(menu_path + "sumcategory.txt", 'w')
for attribute, categorylist in category_entropy_dict.iteritems():
    super_ca_sum_dict = dict()
    plus_supercategory_list = list()
#     print attribute, categorylist
    for unique_category in categorylist:
#         print unique_category
        if unique_category[0] in category_dict:
            for super_ca in category_dict[unique_category[0]]:
                if super_ca not in super_ca_sum_dict:
                    super_ca_sum_dict[super_ca] = 0
                super_ca_sum_dict[super_ca] += int(unique_category[1])
#             print unique_category
        else:
            print unique_category, " not in category_dict"
    supercategory_tuple_dict = sorted(super_ca_sum_dict.items(), key=itemgetter(1), reverse = True)
    for k, v in supercategory_tuple_dict:
        super_file.write("%s\t%s\t%s\n" %(attribute, k, v))
super_file.close()
