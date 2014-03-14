#-*- coding:UTF-8 -*-
'''
Created on 2014年3月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

@input:
refine_entropy.txt
raw_skos.txt

@output:
super_category \t total_category \t have_entropy_category \t attribute \t include_category \t most_value \t include_category2 \n

'''
from collections import Counter

menu_path = "D:\\xubo\\dbpedia\\"

# read refine_entroy.txt file
category_entropy_dict = dict()
refine_file = open(menu_path + "refine_entropy.txt", 'r')
refine_lines = refine_file.readlines()
for line in refine_lines:
    line = line.rstrip()
    words = line.split("\t")
    if words[0] not in category_entropy_dict:
        category_entropy_dict[words[0]] = set()
    category_entropy_dict[words[0]].add((words[1], words[2]))
refine_file.close()

# read raw_skos.txt file
skos_dict = dict()
skos_file = open(menu_path + "raw_skos.txt", 'r')
skos_lines = skos_file.readlines()
for line in skos_lines:
    line = line.rstrip()
    words = line.split("\t")

    if words[1] not in skos_dict:
        skos_dict[words[1]] = set()
    skos_dict[words[1]].add(words[0])
skos_file.close()


template_file = open(menu_path + "category_template.txt", 'w')
for super_ca, sub_cas in skos_dict.iteritems():
    attribute_value_dict = dict()
    attribute_category_dict = dict()
    miss_count = 0
    for sub_ca in sub_cas:
        if sub_ca not in category_entropy_dict:
            miss_count += 1
            continue
        for av in category_entropy_dict[sub_ca]:
            a = av[0]
            v = av[1]
            if a not in attribute_category_dict:
                attribute_category_dict[a] = set()
            if a not in attribute_value_dict:
                attribute_value_dict[a] = list()

            attribute_category_dict[a].add(sub_ca)
            attribute_value_dict[a].append(v)
    
    for at, mvl in attribute_value_dict.iteritems():
#         print ca, len(ens),
#         print at, len(attribute_entity_dict[at]),
        most_value = Counter(mvl).most_common(1)[0]
#         print most_value[0], most_value[1]
        template_file.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(super_ca, str(len(sub_cas)), str(len(sub_cas)- miss_count), at, str(len(attribute_category_dict[at])), most_value[0], str(most_value[1])))

template_file.close()     