#-*- coding:UTF-8 -*-
'''
Created on 2014年3月6日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
from collections import Counter
menu_path = "D:\\xubo\\ENwiki\\origin\\"
#初始化category template
category_template_dict = dict()
template_file = open(menu_path + "refine_entropy.txt", 'r')
template_lines = template_file.readlines()
for line in template_lines:
    line = line.rstrip().lower()
    words = line.split("\t")
    if words[0] not in category_template_dict:
        category_template_dict[words[0]] = list()
    category_template_dict[words[0]].append((words[1], words[2]))

#初始化所有集合
result_file = open(menu_path + "category_template.txt", 'w')
super_file = open(menu_path + "category_group.txt", 'r')
super_lines = super_file.readlines()
for line in super_lines:
    line = line.rstrip().lower()
    words = line.split("\t")
    sub_sizes = len(words) - 1
    super_template_list = list()
    attribute_dict = dict()
    for i in range(1, len(words)):
        for label in category_template_dict[words[i]]:
#             print label
#             print label[0], label[1]
            if label[0] not in attribute_dict:
                attribute_dict[label[0]] = list()
            attribute_dict[label[0]].append(label[1])

    for k, v in attribute_dict.iteritems():
        if len(v) > 5:
            most_common = Counter(v).most_common(1)
            if len(v) * 0.85 < most_common[0][1]:
                result_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" %(words[0], sub_sizes, k, len(v), most_common[0][0], str(most_common[0][1])))
    
result_file.close()