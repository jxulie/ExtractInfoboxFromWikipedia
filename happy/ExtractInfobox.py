#-*- coding:UTF-8 -*-
'''
Created on 2014年1月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: songs produced by 
extract_value = re.findall(pattern, line)
'''
import re
MENU_PATH = "D://xubo//ENwiki//sample//"
CATEGORY_PATH = MENU_PATH + "sample_category_produced.txt"

pattern = re.compile(r'songs produced by (.*)')
entity_attribute_dict = dict()
category_file = open(CATEGORY_PATH, 'r')
category_lines = category_file.readlines()
for line in category_lines:
    line = line.rstrip()
    words = line.split("\t")
    entity = words[0]
    category = words[1]
    extract_value = re.findall(pattern, category)
    attribute = extract_value[0]
    if entity not in entity_attribute_dict:
        entity_attribute_dict[entity] = set()
    entity_attribute_dict[entity].add(attribute)

infobox_path = MENU_PATH + "infobox_from_category.txt"
infobox_file = open(infobox_path, 'w')
for k, v in entity_attribute_dict.iteritems():
    infobox_file.write("%s\t%s\n" %(k,"|".join(v)))
infobox_file.close()
