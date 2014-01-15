#-*- coding:UTF-8 -*-
'''
Created on 2014年1月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: compare the results

'''
MENU_PATH = "D://xubo//ENwiki//sample//"
INFOBOX_PATH = MENU_PATH + "infobox_from_category.txt"
produce_path = MENU_PATH + "produce_infobox.txt"
compare_path = MENU_PATH + "compare_infobox.txt"

infobox_dict = dict()
produce_dict = dict()

infobox_file = open(INFOBOX_PATH, 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    line = line.rstrip()
    words = line.split("\t")
    infobox_dict[words[0]] = words[1]
infobox_file.close()

produce_file = open(produce_path, 'r')
produce_lines = produce_file.readlines()
for line in produce_lines:
    line = line.rstrip()
    words = line.split("\t")
    produce_dict[words[0]] = words[1]
produce_file.close()

infobox_set = set(infobox_dict.keys())
produce_set = set(produce_dict.keys())
common_set = infobox_set.intersection(produce_set)

print "infobox_set: ", len(infobox_set)
print "produce_set: ", len(produce_set)
print "common_set: ", len(common_set)

compare_file = open(compare_path, 'w')
for common in common_set:
    compare_file.write("%s\t%s\t%s\n" % (common, infobox_dict[common], produce_dict[common]))
compare_file.close()
