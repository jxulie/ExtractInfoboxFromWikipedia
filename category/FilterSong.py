#-*- coding:UTF-8 -*-
'''
Created on 2013年12月26日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: filter all the category include song

'''
menu_path = "D://xubo//ENwiki//refine//"
category_entropy_path = menu_path + "category_relation.txt"
filter_category_entropy_path = menu_path + "filter_category_relation.txt"
filter_category_entropy_file = open(filter_category_entropy_path, 'w')
category_entropy_file = open(category_entropy_path, 'r')
category_entropy_lines = category_entropy_file.readlines()
for line in category_entropy_lines:
    if "song" in line:
        filter_category_entropy_file.write(line)
category_entropy_file.close()
filter_category_entropy_file.close()