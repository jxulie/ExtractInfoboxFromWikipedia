#-*- coding:UTF-8 -*-
'''
Created on 2013年12月16日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: sample category from category file

'''
sample_category_file = open("D://xubo//ENwiki//sample_category_produced.txt", 'w')
category_file = open("D://xubo//ENwiki//category_final.txt", 'r')
category_lines = category_file.readlines()
for line in category_lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        entity = words[0]
        category = words[1]
        if "songs produced by" in category:
            sample_category_file.write("%s\t%s\n" %(entity, category))
    except:
        print line
category_file.close()
sample_category_file.close()