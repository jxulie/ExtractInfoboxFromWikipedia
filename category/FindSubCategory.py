#-*- coding:UTF-8 -*-
'''
Created on 2013年12月27日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: find sub category

'''
import nltk
import math
import operator
from collections import Counter

menu_path = "D://xubo//ENwiki//refine//"
super_category_file = open(menu_path + "supercategory.txt", 'r')
lines = super_category_file.readlines()
sub_category_list = list()
for line in lines:
    try:
        line = line.lower().rstrip()
        words = line.split("\t")
        for i in range(1,len(words)):
            if words[i] == "songs by songwriter":
                sub_category_list.append(words[0])
                break
    except:
        print "error : ", line

super_category_file.close()




# menu_path = "D://xubo//ENwiki//refine//"
# entity_category_path = menu_path + "sample_category_final.txt"
# entity_infobox_path = menu_path + "sample_infobox_final3.txt"
# category_attribute_path = menu_path + "wiki_schema_refinered.txt"
# category_entropy_path = menu_path + "wiki_category_entropy.txt"
entity_category_path = menu_path + "category_final.txt"
entity_infobox_path = menu_path + "refine_infobox.txt"
category_attribute_path = menu_path + "schema_refinered.txt"
category_entropy_path = menu_path + "category_entropy.txt"

entity_category_dict = dict()#key:entity value:category list
entity_infobox_dict = dict()#key:entity  value:(attribute, value)
category_attribute_dict = dict()# key:category_attribute value: value

def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])

def have_unique_value(valuelist):
#     print valuelist
    all_value_list = [va for value in valuelist for va in value.split("|") if va != '"' and va != ""]
    c = Counter(all_value_list).most_common()
    if len(c) > 0:
        clist = [k[0] for k in c]
    #     print clist
        result = clist[0]
        for i in range(1,len(valuelist)):
            if result not in valuelist[i]:
                result = None
                break
        return result
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




for aaa in sub_category_list:
    if (aaa, "writer") in category_attribute_dict:
        print category_attribute_dict[(aaa, "writer")]

