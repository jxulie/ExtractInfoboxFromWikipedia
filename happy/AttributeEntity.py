#-*- coding:UTF-8 -*-
'''
Created on 2014年1月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''

MENU_PATH = "D://xubo//ENwiki//sample//"
INFOBOX_PATH = MENU_PATH + "sample_infobox_split_produced.txt"
produce_path = MENU_PATH + "produce_infobox.txt"


infobox_file = open(INFOBOX_PATH, 'r')
infobox_lines = infobox_file.readlines()
produce_file = open(produce_path, 'w')
for line in infobox_lines:
    line = line.rstrip()
    words = line.split("\t")
    if words[1] == "producer":
        produce_file.write("%s\t%s\n" %(words[0], words[2]))
produce_file.close()
