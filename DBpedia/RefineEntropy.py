#-*- coding:UTF-8 -*-
'''
Created on 2014年3月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''

menu_path = "D:\\xubo\\dbpedia\\"

entropy_file = open(menu_path + "filter_entropy.txt", 'r')
entropy_lines = entropy_file.readlines()

refined_file = open(menu_path + "refine_entropy.txt", 'w')
for line in entropy_lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        category = words[0]
        attribute = words[2]
        value = words[4]
        if value in category:
            value = category.replace(value, "jxulie")
        refined_file.write("%s\t%s\t%s\n" %(category, attribute, value))
    except:
        print "error", line
refined_file.close()
