#-*- coding:UTF-8 -*-
'''
Created on 2014年3月6日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
import re


entropy_file = open("D:\\xubo\\ENwiki\\origin\\all_filter_entropy.txt", 'r')
entropy_lines = entropy_file.readlines()

refined_file = open("D:\\xubo\\ENwiki\\origin\\refine_entropy.txt", 'w')
for line in entropy_lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        category = words[0]
        attribute = words[1]
        value = words[2]
        if value in category:
            value = re.sub("\\b"+ value+ "\\b", "jxulie", category)
        refined_file.write("%s\t%s\t%s\n" %(category, attribute, value))
    except:
        print "error", line
refined_file.close()
