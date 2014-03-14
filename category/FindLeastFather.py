#-*- coding:UTF-8 -*-
'''
Created on 2014年3月6日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 找到所有category对应的最低父节点，类似于最小集合覆盖

@method:

所有节点 category set
所有集合 sets_dict
'''
#导入所有节点
import pickle
import copy

pickle_file = open("D:\\xubo\\ENwiki\\origin\\unique_category.pickle", 'rb')
category_set = pickle.load(pickle_file)

#初始化所有集合
sets_dict = dict()
super_file = open("D:\\xubo\\ENwiki\\origin\\eng_superCategory_clean.txt", 'r')
super_lines = super_file.readlines()
for line in super_lines:
    line = line.rstrip().lower()
    words = line.split("\t")
    if len(words) > 1 and words[0] in category_set:
        for i in range(1, len(words)):
            if words[i] not in sets_dict:
                sets_dict[words[i]] = set()
            sets_dict[words[i]].add(words[0])
            
#集合概率 贪心算法
final_file = open("D:\\xubo\\ENwiki\\origin\\category_group.txt", 'w')
final_set = set()
while(True):
    current_size = len(final_set)
    current_set = copy.copy(final_set)
    current_k = None
    current_v = None
    changed = False
    temp_set = None
    for k, v in sets_dict.iteritems():
#         print k, v
        temp_set = current_set.union(v)
        if len(temp_set) > current_size:
            current_size = len(temp_set)
#             current_set = copy.copy(temp_set)
            current_k = k
            current_v = v
            changed = True
    
    if  changed == False:
        break
    if len(current_v) < 5:
        break
    current_set = copy.copy(current_set.union(current_v))
    final_set = copy.copy(current_set)       
    final_file.write("%s\t%s\n" %(current_k, "\t".join(current_v)))
final_file.close()
