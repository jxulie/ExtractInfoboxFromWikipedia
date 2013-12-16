#-*- coding:UTF-8 -*-
'''
Created on 2013年12月15日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Filter category and infobox 

'''
special_set = set()
special_file = open("D://xubo//ENwiki//special", 'r')
special_lines = special_file.readlines()
for line in special_lines:
    line = line.rstrip()
    special_set.add(line)
print "special set ok"
new_category_file = open("D://xubo//ENwiki//new_wiki_category.txt", 'w')
category_file = open("D://xubo//ENwiki//ENwikicategory.txt", 'r')
category_lines = category_file.readlines()
for line in category_lines:
    line = line.rstrip()
    words = line.split("\t")
    if len(words) > 1:
        if words[0] not in special_set:
            new_category_file.write(line + "\n")
category_file.close()
new_category_file.close()
print "category ok"
new_infobox_file = open("D://xubo//ENwiki//new_wiki_infobox.txt", 'w')
infobox_file = open("D://xubo//ENwiki//ENwikiinfobox.txt", 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    line = line.rstrip()
    words = line.split("\t")
    if len(words) > 1:
        if words[0] not in special_set:
            new_infobox_file.write(line + "\n")
infobox_file.close()
new_infobox_file.close()
print "infobox ok"