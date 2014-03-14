#-*- coding:UTF-8 -*-
'''
Created on 2014年3月9日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

从底部开始扩展，看最后能到哪一层

@input:
refine_entropy.txt

'''

#导入所有节点
import pickle
import copy
menu_path = "D:\\xubo\\ENwiki\\origin\\"
pickle_file = open(menu_path + "unique_category.pickle", 'rb')
category_set = pickle.load(pickle_file)

#初始化所有集合
sub_category_dict = dict()
sub_file = open("D:\\xubo\\ENwiki\\origin\\eng_superCategory_clean.txt", 'r')
sub_lines = sub_file.readlines()
for line in sub_lines:
    line = line.rstrip().lower()
    words = line.split("\t")
    sub_category_dict[words[0]] = words[1:]

sub_file.close()


           
# #集合概率 贪心算法
# final_file = open("D:\\xubo\\ENwiki\\origin\\category_group.txt", 'w')
# final_set = set()
# while(True):
#     current_size = len(final_set)
#     current_set = copy.copy(final_set)
#     current_k = None
#     current_v = None
#     changed = False
#     temp_set = None
#     for k, v in sets_dict.iteritems():
# #         print k, v
#         temp_set = current_set.union(v)
#         if len(temp_set) > current_size:
#             current_size = len(temp_set)
# #             current_set = copy.copy(temp_set)
#             current_k = k
#             current_v = v
#             changed = True
#     
#     if  changed == False:
#         break
#     if len(current_v) < 5:
#         break
#     current_set = copy.copy(current_set.union(current_v))
#     final_set = copy.copy(current_set)       
#     final_file.write("%s\t%s\n" %(current_k, "\t".join(current_v)))
# final_file.close()

