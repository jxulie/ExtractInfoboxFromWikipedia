#-*- coding:UTF-8 -*-
'''
Created on 2013年12月16日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: sample infobox

'''
entity_set = set()
sample_category_file = open("D://xubo//ENwiki//sample_category_produced.txt", 'r')
category_lines = sample_category_file.readlines()
for line in category_lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        entity = words[0]
        entity_set.add(entity)
    except:
        print line
sample_category_file.close()
sample_infobox_file = open("D://xubo//ENwiki//sample_infobox_produced.txt", 'w')
# infobox_file = open("D://xubo//ENwiki//infobox_final.txt", 'r')
infobox_file = open("D://xubo//ENwiki//new_infobox.txt", 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        entity = words[0]
        if entity in entity_set:
            sample_infobox_file.write(line + "\n")
    except:
        print line
infobox_file.close()
sample_infobox_file.close()