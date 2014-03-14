#-*- coding:UTF-8 -*-
'''
Created on 2014年3月11日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
menu_path = "G:\\xubo\\"
menu_path2 = "D:\\xubo\\dbpedia\\"
raw_skos_file = open(menu_path2 + "raw_skos.txt", 'w')
category_file = open(menu_path + "skos_categories_en.nt", 'r')
category_lines = category_file.readlines()
for line in category_lines:
    try:
        line = line.rstrip()
        words = line.split(" ")
        if len(words) == 4:
    #     print line
            if words[0].startswith("<http://dbpedia.org/resource/Category:") and words[1] == "<http://www.w3.org/2004/02/skos/core#broader>" and words[2].startswith("<http://dbpedia.org/resource/Category:"):
                entity = words[0][38:-1]
                
                category = words[2][38:-1]
                
                
#                 print entity, category
                raw_skos_file.write("%s\t%s\n" %(entity, category))
            else:
#                 print line
                continue
    except:
        print "error: ", line
raw_skos_file.close()