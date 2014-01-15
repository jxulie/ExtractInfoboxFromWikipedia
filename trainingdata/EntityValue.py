#-*- coding:UTF-8 -*-
'''
Created on 2014年1月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Construct (attribute, sentence, value) training data

input:

attribute:
album
artist
genre
length
producer
recorded
released
writer



'''

MENU_PATH = "D://xubo//ENwiki//sample//"
INFOBOX_PATH = MENU_PATH + "sample_infobox_split_produced.txt"
CATEGORY_PATH = MENU_PATH + "sample_category_produced.txt"
SCHEMA_PATH = MENU_PATH + "sample_schema_produced.txt"
SCHEMA_ENTITY_VALUE_MENU = MENU_PATH + "newtrainset1\\"
ATTRIBUTE_PATH = MENU_PATH + "sample_attribute.txt"

attribute_dict = dict()


attribute_file = open(ATTRIBUTE_PATH, 'r')
attribute_lines = attribute_file.readlines()
for line in attribute_lines:
    line = line.rstrip()
    attribute_dict[line] = set()
    
infobox_file = open(INFOBOX_PATH, 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    line = line.rstrip()
    words = line.split("\t")
    if words[1] in attribute_dict:
        attribute_dict[words[1]].add((words[0], words[2]))

for k, v in attribute_dict.iteritems():
    write_file = open(SCHEMA_ENTITY_VALUE_MENU + k, 'w')
    for v1 in v:
        write_file.write("%s\t%s\n" %(v1[0], v1[1]))
    write_file.close()
