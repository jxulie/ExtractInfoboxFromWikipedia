#-*- coding:UTF-8 -*-
'''
Created on 2013年12月16日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Statistic category num

'''
import operator
category_num_dict = dict()

category_file = open("D://xubo//ENwiki//new_pair_category.txt", 'r')
category_lines = category_file.readlines()
for line in category_lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        entity = words[0]
        category = words[1]
        if category not in category_num_dict:
            category_num_dict[category] = 0
        category_num_dict[category] += 1
    except:
        print line
category_file.close()

category_num_file = open("D://xubo//ENwiki//category_num.txt", 'w')
for k,v in sorted(category_num_dict.iteritems(), key=operator.itemgetter(1), reverse = True):
    category_num_file.write("%s\t%s\n" %(k, str(v)))
category_num_file.close()