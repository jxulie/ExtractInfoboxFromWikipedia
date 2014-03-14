#-*- coding:UTF-8 -*-
'''
Created on 2013年12月25日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: statistic category 

'''
import nltk
menu_path = "D:\\xubo\\dbpedia\\"
category_file = open(menu_path + "raw_category.txt", 'r')
category_lines = category_file.readlines()
category_list = list()
for line in category_lines:
    try:
        category = line.rstrip().split("\t")[1]
        category_list.append(category)
    except:
        print "error : ", line
category_info = nltk.FreqDist(category_list) 
# print category_info
category_info_file = open(menu_path + "statistic_raw_category.txt", 'w')
for k,v in category_info.iteritems():
    category_info_file.write("%s\t%s\n" %(k, v))
category_info_file.close()
