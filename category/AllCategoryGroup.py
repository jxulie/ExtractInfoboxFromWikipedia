#-*- coding:UTF-8 -*-
'''
Created on 2014年3月7日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
unique_template_category = set()
unique_file = open("D:\\xubo\\ENwiki\\origin\\unique_template_category.txt", 'r')
unique_lines = unique_file.readlines()
for line in unique_lines:
    line = line.rstrip()
    unique_template_category.add(line)
unique_file.close()

#初始化所有集合
sets_dict = dict()
super_file = open("D:\\xubo\\ENwiki\\origin\\eng_superCategory_clean.txt", 'r')
super_lines = super_file.readlines()
for line in super_lines:
    line = line.rstrip().lower()
    words = line.split("\t")
    if len(words) > 1:
        for i in range(1, len(words)):
            if words[i] in unique_template_category:
                if words[i] not in sets_dict:
                    sets_dict[words[i]] = set()
                sets_dict[words[i]].add(words[0])

all_category_group_file = open("D:\\xubo\\ENwiki\\origin\\all_category_group.txt", 'w')
for k, v in sets_dict.iteritems():
    all_category_group_file.write("%s\t%s\n" % (k, "\t".join(v)))
all_category_group_file.close()