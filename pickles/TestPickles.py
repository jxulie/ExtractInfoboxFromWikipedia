#-*- coding:UTF-8 -*-
'''
Created on 2014年3月4日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
import pickle
pickle_file = open("D:\\xubo\\ENwiki\\article_id.pickle", 'rb')
test_dict = pickle.load(pickle_file)
print test_dict