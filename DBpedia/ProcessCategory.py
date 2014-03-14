#-*- coding:UTF-8 -*-
'''
Created on 2014年3月11日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

subject: start with <http://dbpedia.org/resource/***>

predict: <http://purl.org/dc/terms/subject>

object: <http://dbpedia.org/resource/Category:***>
'''


menu_path = "G:\\xubo\\"
menu_path2 = "D:\\xubo\\dbpedia\\"
raw_category_file = open(menu_path2 + "raw_category.txt", 'w')
category_file = open(menu_path + "article_categories_en.nt", 'r')
category_lines = category_file.readlines()
for line in category_lines:
    try:
        line = line.rstrip()
        words = line.split(" ")
        if len(words) == 4:
    #     print line
            if words[0].startswith("<http://dbpedia.org/resource/") and words[1] == "<http://purl.org/dc/terms/subject>" and words[2].startswith("<http://dbpedia.org/resource/Category:"):
                entity = words[0][29:-1]
                
                category = words[2][38:-1]
                
                
#                 print entity, category
                raw_category_file.write("%s\t%s\n" %(entity, category))
            else:
                print "line"
                continue
    except:
        print "error: ", line
raw_category_file.close()
