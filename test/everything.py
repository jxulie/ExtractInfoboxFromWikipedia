#-*- coding:UTF-8 -*-
'''
Created on 2013年12月15日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Test everything

'''

# test strip() function
# aaa = " After a few years in the 2nd highest division, they won the qualifying tournament for the 2012-13 season "
# print aaa
# print aaa.lstrip()
# print aaa.rstrip()
# print aaa.strip()

# test file
NEW_ARTICLE_MENU = "D:\\xubo\\ENwiki\\newdata2\\"
test_file = open(NEW_ARTICLE_MENU + "1000.txt", 'r')
test_lines = test_file.readlines()
print len(test_lines)
for line in test_lines:
    print line.rstrip()