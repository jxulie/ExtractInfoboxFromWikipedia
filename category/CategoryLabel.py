#-*- coding:UTF-8 -*-
'''
Created on 2014年3月7日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

D:\\xubo\\ENwiki\\origin\\category_group.txt
D:\\xubo\\ENwiki\\origin\\category_template.txt

'''
import re

template_dict = dict()
template_file = open("D:\\xubo\\ENwiki\\origin\\category_template.txt", 'r')
template_lines = template_file.readlines()
for line in template_lines:
    line = line.rstrip()
    words = line.split("\t")
    category = words[0]
    attribute = words[2]
    value = words[4]
    if category not in template_dict:
        template_dict[category] = set()
    template_dict[category].add((attribute, value))

print "ok"

category_label_file = open("D:\\xubo\\ENwiki\\origin\\category_label.txt", 'w')
super_file = open("D:\\xubo\\ENwiki\\origin\\all_category_group.txt", 'r')
super_lines = super_file.readlines()
for line in super_lines:
    line = line.rstrip()
    words = line.split("\t")
    if words[0] in template_dict:
        for label in template_dict[words[0]]:
            if "jxulie" not in label[1]:
                for i in range(1, len(words)):
                    category_label_file.write("%s\t%s\t%s\n" %(words[i], label[0], label[1]))
            else:
                for i in range(1, len(words)):
                    temp_string = label[1].replace("jxulie", "(.*)")
                    pattern = re.compile(temp_string)
                    extract_value = re.findall(pattern, words[i])
                    if len(extract_value) > 0:
                        category_label_file.write("%s\t%s\t%s\n" %(words[i], label[0], extract_value[0]))

category_label_file.close()
