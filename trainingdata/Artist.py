#-*- coding:UTF-8 -*-
'''
Created on 2014年1月14日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''

MENU_PATH = "D://xubo//ENwiki//sample//"
artist_path = MENU_PATH + "newtrainset1\\artist"
new_path = MENU_PATH + "newtrainset1\\new_artist"
artist_file = open(artist_path, 'r')
new_file = open(new_path, 'w')
lines = artist_file.readlines()
for line in lines:
    line = line.rstrip()
    words = line.split("\t")
    attribute = words[1]
    if attribute.find("|featuring") != -1:
        attribute = attribute[:attribute.find("|featuring")]
    new_file.write("%s\t%s\n" %(words[0], attribute))
new_file.close()
artist_file.close()



