#-*- coding:UTF-8 -*-
'''
Created on 2014年3月11日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''

aaa = '"4\u00D7 Platinum (RIAA)"@en'

print  aaa[aaa.find('"')+1:aaa.rfind('"')]