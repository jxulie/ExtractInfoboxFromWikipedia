#-*- coding:UTF-8 -*-
'''
Created on 2014年3月7日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
category_set = set()
entropy_file = open("D:\\xubo\\ENwiki\\origin\\category_template.txt", 'r')
entropy_lines = entropy_file.readlines()

for line in entropy_lines:
    line = line.rstrip()
    words = line.split("\t")
    category_set.add(words[0])
    
unique_file = open("D:\\xubo\\ENwiki\\origin\\unique_template_category.txt", 'w')
for uni in category_set:
    unique_file.write("%s\n" % uni)
unique_file.close()