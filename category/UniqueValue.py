#-*- coding:UTF-8 -*-
'''
Created on 2013年12月25日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: find unique value from category schema

'''
import nltk
import math
import operator
from collections import Counter

menu_path = "D://xubo//ENwiki//origin//"
entity_category_path = menu_path + "all_category.txt"
entity_infobox_path = menu_path + "all_infobox.txt"
category_attribute_path = menu_path + "all_schema.txt"
category_entropy_path = menu_path + "all_entropy.txt"
# MENU_PATH = "D://xubo//ENwiki//origin//"
# INFOBOX_PATH = MENU_PATH + "all_infobox.txt"
# CATEGORY_PATH = MENU_PATH + "all_category.txt"
# SCHEMA_PATH = MENU_PATH + "all_schema.txt"
# entity_category_path = menu_path + "category_final.txt"
# entity_infobox_path = menu_path + "refine_infobox.txt"
# category_attribute_path = menu_path + "schema_refinered.txt"
# category_entropy_path = menu_path + "category_entropy.txt"

entity_category_dict = dict()#key:entity value:category list
entity_infobox_dict = dict()#key:entity  value:(attribute, value)
category_attribute_dict = dict()# key:category_attribute value: value
category_entity_dict = dict()#key:category value:entity set
attribute_entity_dict = dict()#key:attribute value:entity set

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])

def have_unique_value(valuelist):
#     print valuelist
    common_num = 0
    result = None
    all_value_list = [va for value in valuelist for va in value.split("|") if va != '"' and va != ""]
    c = Counter(all_value_list).most_common()
    if len(c) > 0:
        clist = [k[0] for k in c]
    #     print clist
        result = clist[0]
        common_num += 1
        for i in range(1,len(valuelist)):
            if result in valuelist[i]:
                common_num += 1
    return result, common_num
# c = Counter(alllist).most_common()
# # print c.most_common()
# # print sorted(c)
# clist = [k[0] for k in c]
# print clist
# print clist[0]
entity_category_file = open(entity_category_path, 'r')
lines = entity_category_file.readlines()
for line in lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        entity = words[0]
        category = words[1]
        if entity not in entity_category_dict:
            entity_category_dict[entity] = list()
        entity_category_dict[entity].append(category)
        
        if category not in category_entity_dict:
            category_entity_dict[category] = set()
        category_entity_dict[category].add(entity)
    except:
        print line
entity_category_file.close()



entity_infobox_file = open(entity_infobox_path, 'r')
lines = entity_infobox_file.readlines()
for line in lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        entity = words[0]
        attribute = words[1]
        value = words[2]
        if entity not in entity_infobox_dict:
            entity_infobox_dict[entity] = list()
        entity_infobox_dict[entity].append((attribute, value))
        
        if attribute not in attribute_entity_dict:
            attribute_entity_dict[attribute] = set()
        attribute_entity_dict[attribute].add(entity)
    except:
        print line
entity_infobox_file.close()



category_attribute_file = open(category_attribute_path, 'r')
lines = category_attribute_file.readlines()
for line in lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        category = words[0]
        attribute = words[1]
        category_attribute_dict[(category, attribute)] = list()
    except:
        print line
category_attribute_file.close()


for entity, categorylist in entity_category_dict.iteritems():
    if entity not in entity_infobox_dict:
        continue
    infoboxlist = entity_infobox_dict[entity]
    for category in categorylist:
        for infobox in infoboxlist:
            attribute = infobox[0]
            value = infobox[1]
            if (category, attribute) not in category_attribute_dict:
                continue
            category_attribute_dict[(category, attribute)].append(value)


category_entropy_dict = dict()
for category_attribute, value in category_attribute_dict.iteritems():
    unique_value = have_unique_value(value)
    if unique_value[0] != None and unique_value[0] != '"':
        category_entropy_dict[(category_attribute[0], category_attribute[1])] = (unique_value[0], unique_value[1], len(value))
#     category_entropy_file.write("%s\t%s\t%s\t%s\n" %(category_attribute[0], category_attribute[1], len(value), entropy(value))) 


sorted_category_entropy_list = sorted(category_entropy_dict.iteritems(), key=operator.itemgetter(0))

category_entropy_file = open(category_entropy_path, 'w')
for category_attribute, value in sorted_category_entropy_list:
    category_entropy_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" %(category_attribute[0], category_attribute[1], value[0], str(value[1]), str(len(attribute_entity_dict[category_attribute[1]].intersection(category_entity_dict[category_attribute[0]]))), str(len(category_entity_dict[category_attribute[0]])))) 
category_entropy_file.close()
