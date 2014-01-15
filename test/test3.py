#-*- coding:UTF-8 -*-
'''
Created on 2013年12月26日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

# (14, "'' is the title of a song recorded by american country music artist jxulie"): 19
# (13, 'is the title of a song recorded by american country music artist jxulie'): 19
# (12, 'the title of a song recorded by american country music artist jxulie'): 19
# (11, 'title of a song recorded by american country music artist jxulie'): 19
# (10, 'of a song recorded by american country music artist jxulie'): 19
# (10, "'' is a song by jxulie , released as the"): 14
# (9, 'is a song by jxulie , released as the'): 14
# (9, 'co-written and recorded by american country music singer jxulie'): 11
# (9, 'a song recorded by american country music artist jxulie'): 20
# (9, "'' is a song by jxulie , released as"): 20
# (9, "'' is a song by american recording artist jxulie"): 20
# (8, 'song recorded by american country music artist jxulie'): 20
# (8, 'is a song by jxulie , released as'): 20
# (8, 'is a song by american recording artist jxulie'): 20
# (8, 'and recorded by american country music singer jxulie'): 22
# (8, 'and recorded by american country music artist jxulie'): 23
# (8, 'a song by jxulie , released as the'): 14
# '''
# 
# set1 = set()
# set1.add("'' is the title of a song recorded by american country music artist jxulie")
# set1.add("'' is a song by jxulie , released as the")
# 
# aaa = 'is the title of a song recorded by american country music artist jxulie'
# flag = False
# for se in set1:
#     if aaa in se:
#         flag = True
#         break
# if flag == True:
#     print "yes"
# else:
#     print "no"
#         


test_file = open("D://xubo//ENwiki//newdata//999975.txt", 'r')
print test_file.read()