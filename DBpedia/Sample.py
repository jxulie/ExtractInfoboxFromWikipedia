#-*- coding:UTF-8 -*-
'''
Created on 2014年3月12日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''

sample_num = 100000
menu_path = "D:\\xubo\\dbpedia\\"

infobox_dict = dict()
infobox_file = open(menu_path + "raw_infobox.txt", 'r')
sample_infobox_file = open(menu_path + "raw_infobox_sample.txt", 'w')
infobox_lines = infobox_file.readlines()
count1 = 0
for line in infobox_lines:
    count1 += 1
    if count1 > sample_num:
        break
    line = line.rstrip()
    sample_infobox_file.write(line + "\n")
infobox_file.close()
sample_infobox_file.close()

category_dict = dict()
category_file = open(menu_path + "raw_category.txt", 'r')
sample_category_file = open(menu_path + "raw_category_sample.txt", 'w')
category_lines = category_file.readlines()
count2 = 0
for line in category_lines:
    count2 += 1
    if count2 > sample_num:
        break
    line = line.rstrip()
    line = line.rstrip()
    sample_category_file.write(line + "\n")

category_file.close()
sample_category_file.close()
