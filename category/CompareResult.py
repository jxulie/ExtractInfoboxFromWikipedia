#-*- coding:UTF-8 -*-
'''
Created on 2014年3月9日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
MENU_PATH = "D://xubo//ENwiki//origin//"
infobox_path = MENU_PATH + "all_infobox.txt"
triple_path = MENU_PATH + "new_triples.txt"

infobox_set = set()
triple_set = set()

infobox_file = open(infobox_path, 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    line = line.rstrip()
    words = line.split("\t")
    infobox_set.add((words[0], words[1]))


triple_file = open(triple_path, 'r')
triple_lines = triple_file.readlines()
for line in triple_lines:
    line = line.rstrip()
    words = line.split("\t")
    triple_set.add((words[0], words[1]))

print "infobox_set :", len(infobox_set)
print "triple_set :", len(triple_set)
print "intersection set :", len(infobox_set.intersection(triple_set))