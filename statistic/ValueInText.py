#-*- coding:UTF-8 -*-
'''
Created on 2014年3月4日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
import pickle
pickle_file = open("D:\\xubo\\ENwiki\\article_id.pickle", 'rb')
article_id_dict = pickle.load(pickle_file)

menu_path = "D://xubo//ENwiki//origin//"
entity_infobox_path = menu_path + "all_infobox.txt"
file_path = "D:\\xubo\\ENwiki\\nltk_newdata\\"

result_path = menu_path + "all_infobox_statistic.txt"
result_file = open(result_path, 'w')


infobox_file = open(entity_infobox_path, 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    line = line.rstrip()
    words = line.split("\t")
    entity = words[0]
    attribute = words[1]
    values = words[2]
    try:
        temp_file = open(file_path + article_id_dict[entity], 'r')
        if any (value in temp_file.read().lower() for value in values.split("|")):
            result_file.write("%s\t%s\n" % (line, "1"))
        else:
            result_file.write("%s\t%s\n" % (line, "0"))
    except:
        result_file.write("%s\t%s\n" % (line, "0"))
    finally:
        temp_file.close()
