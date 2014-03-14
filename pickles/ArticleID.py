#-*- coding:UTF-8 -*-
'''
Created on 2014年3月4日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: pickle article id

'''
import pickle

article_id_dict = dict()
article_id_path = "D:\\xubo\\ENwiki\\article_id"
article_id_file = open(article_id_path, 'r')
article_id_lines = article_id_file.readlines()
for line in article_id_lines:
    line = line.rstrip()
    words = line.split("\t")
    article_id_dict[words[0]] = words[1]

id_pickle_path = "D:\\xubo\\ENwiki\\article_id.pickle"
id_pickle_file = open(id_pickle_path, 'wb')
pickle.dump(article_id_dict, id_pickle_file)
id_pickle_file.close()