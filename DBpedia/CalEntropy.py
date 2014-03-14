#-*- coding:UTF-8 -*-
'''
Created on 2014年3月11日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: find the unique value in category 

@input:
raw_infobox.txt
raw_category.txt

@output:
category \t total_entity \t attribute \t include_entity \t most_value \t include_entity2 \n
'''
from collections import Counter

menu_path = "D:\\xubo\\dbpedia\\"

#output infobox_dict   key:entity  \t value: (attribute,value) set
infobox_dict = dict()
infobox_file = open(menu_path + "raw_infobox.txt", 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    line = line.rstrip()
    words = line.split("\t")
    if words[0] not in infobox_dict:
        infobox_dict[words[0]] = set()
    infobox_dict[words[0]].add((words[1], words[2]))
infobox_file.close()

#output category_dict   key:category  \t value: (entity) set
category_dict = dict()
category_file = open(menu_path + "raw_category.txt", 'r')
category_lines = category_file.readlines()
for line in category_lines:
    line = line.rstrip()
    words = line.split("\t")
    if words[0] not in infobox_dict:
        continue
    if words[1] not in category_dict:
        category_dict[words[1]] = set()

    category_dict[words[1]].add(words[0])    
category_file.close()

entropy_file = open(menu_path + "entropy.txt", 'w')
for ca, ens in category_dict.iteritems():
    attribute_value_dict = dict()
    attribute_entity_dict = dict()
    for en in ens:
        for av in infobox_dict[en]:
            a = av[0]
            v = av[1]
            if a not in attribute_entity_dict:
                attribute_entity_dict[a] = set()
            if a not in attribute_value_dict:
                attribute_value_dict[a] = list()

            attribute_entity_dict[a].add(en)
            attribute_value_dict[a].append(v)
    
    for at, mvl in attribute_value_dict.iteritems():
#         print ca, len(ens),
#         print at, len(attribute_entity_dict[at]),
        most_value = Counter(mvl).most_common(1)[0]
#         print most_value[0], most_value[1]
        entropy_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" %(ca, str(len(ens)), at, str(len(attribute_entity_dict[at])), most_value[0], str(most_value[1])))

entropy_file.close()       
                

# # cal category unique_attribute_num total_attribute_num
# entropy_file = open(menu_path + "entropy.txt", 'w')
# for ca, infos in category_dict.iteritems():
#     entity_count = len(category_entity_dict[ca])
#     attr_dict = dict()
#     for info in infos:
#         if info[0] not in attr_dict:
#             attr_dict[info[0]] = list()
#         attr_dict[info[0]].append(info[1])
#     for attr, vas in attr_dict.iteritems():
#         max_value = Counter(vas).most_common(1)[0]
# #         print max_value
#         if len(vas) > entity_count * 0.3:
#             if max_value[1] > len(vas) * 0.9:
#                 entropy_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" %(ca, str(entity_count), attr, str(len(vas)), max_value[0], str(max_value[1])))
#         
# entropy_file.close()