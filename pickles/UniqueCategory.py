#-*- coding:UTF-8 -*-
'''
Created on 2014年3月6日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
import pickle

category_set = set()
input_path = "D:\\xubo\\ENwiki\\origin\\unique_category.txt"
input_file = open(input_path, 'r')
input_lines = input_file.readlines()
for line in input_lines:
    line = line.rstrip()
    category_set.add(line)

output_path = "D:\\xubo\\ENwiki\\origin\\unique_category.pickle"
output_pickle_file = open(output_path, 'wb')
pickle.dump(category_set, output_pickle_file)
output_pickle_file.close()