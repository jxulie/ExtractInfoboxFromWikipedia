#-*- coding:UTF-8 -*-
'''
Created on 2014年3月6日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
aaa = set()
aaa.add("a")
aaa.add("b")

bbb = set()
bbb.add("c")
bbb = bbb.union(aaa)
print bbb
aaa.add("d")
print aaa
print bbb