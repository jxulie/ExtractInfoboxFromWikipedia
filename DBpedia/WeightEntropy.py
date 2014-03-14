#-*- coding:UTF-8 -*-
'''
Created on 2014年3月14日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: consider weight in entropy

@input:
entropy.txt

@output:
category attribute weight

@规则:
权值为1的情况
category中实体数大于5，属性包含的实体数要占30%，最大value的entity数等于属性包含的entity数

即： 在category \t total_entity \t attribute \t include_entity \t most_value \t include_entity2 \n 中

total_entity > 5 and  include_entity > total_entity * 0.3 and  include_entity == include_entity2 

权值为-1的情况

include_entity2 < include_entity * 0.5

权值为0的情况
else
'''

menu_path = "D:\\xubo\\dbpedia\\"

filter_entropy_file = open(menu_path + "weight_entropy.txt", 'w')
raw_entropy_file = open(menu_path + "entropy.txt", "r")
raw_entropy_lines = raw_entropy_file.readlines()
for line in raw_entropy_lines:
    line = line.rstrip()
    words = line.split("\t")
    category = words[0]
    total_entity = int(words[1])
    attribute = words[2]
    include_entity = int(words[3])
    most_value = words[4]
    include_entity2 = int(words[5])
    if total_entity > 5 and  include_entity > total_entity * 0.5 and  include_entity == include_entity2:
        filter_entropy_file.write("%s\t%s\t%d\n" % (category, attribute, 1))
    elif include_entity * 0.5 > include_entity2:
        filter_entropy_file.write("%s\t%s\t%d\n" % (category, attribute, -1))
    else:
        filter_entropy_file.write("%s\t%s\t%d\n" % (category, attribute, 0))
raw_entropy_file.close()
filter_entropy_file.close()
