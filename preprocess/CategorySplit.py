#-*- coding:UTF-8 -*-
'''
Created on 2013年12月16日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Split N-triple category to pair category

'''
new_category_file = open("D://xubo//ENwiki//new_pair_category.txt", 'w')
category_file = open("D://xubo//ENwiki//new_wiki_category.txt", 'r')
category_lines = category_file.readlines()
for line in category_lines:
    line = line.rstrip()
    words = line.split("\t")
    if len(words) > 1:
        entity = words[0]
        for i in range(1,len(words)):
            if words[i] != "" or words[i] != " ":
                new_category_file.write("%s\t%s\n" %(entity, words[i]))
category_file.close()
new_category_file.close()