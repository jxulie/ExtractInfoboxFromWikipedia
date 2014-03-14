#-*- coding:UTF-8 -*-
'''
Created on 2014年3月7日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: create new triples

'''
category_label_dict = dict()
category_label_file = open("D:\\xubo\\ENwiki\\origin\\category_label.txt", 'r')
category_label_lines = category_label_file.readlines()
for line in category_label_lines:
    line = line.rstrip()
    words = line.split("\t")
    category = words[0]
    attribute = words[1]
    value = words[2]
    if category not in category_label_dict:
        category_label_dict[category] = set()
    category_label_dict[category].add((attribute, value))


infobox_dict = dict() 
article_category_file = open("D:\\xubo\\ENwiki\\origin\\all_category.txt", 'r')
article_category_lines = article_category_file.readlines()
for line in article_category_lines:
    try:
        line = line.rstrip()
        words = line.split("\t")
        if words[1] in category_label_dict:
            if words[0] not in infobox_dict:
                infobox_dict[words[0]] = set()
            infobox_dict[words[0]] = infobox_dict[words[0]].union(category_label_dict[words[1]])
    except:
        print line

new_triple_file = open("D:\\xubo\\ENwiki\\origin\\new_triples.txt", 'w')
for k, v in infobox_dict.iteritems():
    label_dict = dict()
    for v1 in v:
        attribute1 = v1[0]
        value1 = v1[1]
        if attribute1 not in label_dict:
            label_dict[attribute1] = set()
        label_dict[attribute1].add(value1)
    for kk1, vv1 in label_dict.iteritems():
        new_triple_file.write("%s\t%s\t%s\n" %(k, kk1, "|".join(vv1)))
new_triple_file.close()