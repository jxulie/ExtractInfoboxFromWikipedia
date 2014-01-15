#-*- coding:UTF-8 -*-
'''
Created on 2013年12月27日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: find the +1 attribute, category

step:1
for each attribute, find unique category

step2;
for each attribute, find the common super category
'''
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

# for k, v in category_dict.iteritems():
#     print k, v
print len(category_dict)
if "Italian drama television series" in category_dict:
    print "yes, it is in"
else:
    print "no, it is not"

category_entropy_dict = dict()
category_entropy_file = open(menu_path + "filter_category_entropy.txt", 'r')
category_entropy_lines = category_entropy_file.readlines()
for line in category_entropy_lines:
    line = line.rstrip()
    words = line.split("\t")
    category = words[0]
    attribute = words[1]
#     value = words[2]
    if attribute not in category_entropy_dict:
        category_entropy_dict[attribute] = list()
    category_entropy_dict[attribute].append(category)
category_entropy_file.close()

print len(category_entropy_dict)

super_file = open(menu_path + "super.txt", 'w')
for attribute, categorylist in category_entropy_dict.iteritems():
    plus_supercategory_list = list()
#     print attribute, categorylist
    for unique_category in categorylist:
#         print unique_category
        if unique_category in category_dict:
#             print unique_category
            plus_supercategory_list.extend(category_dict[unique_category])
        else:
            print unique_category, " not in category_dict"
    supercategory_tuple_list = Counter(plus_supercategory_list).most_common()
    for supercategory_tuple in supercategory_tuple_list:
        super_file.write("%s\t%s\t%s\n" %(attribute, supercategory_tuple[0], supercategory_tuple[1]))
super_file.close()
