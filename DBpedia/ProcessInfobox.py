#-*- coding:UTF-8 -*-
'''
Created on 2014年3月9日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: process infobox from dbpedia

subject: start with <http://dbpedia.org/resource/***>

predict: <http://dbpedia.org/ontology/***>

object: <http://dbpedia.org/resource/***> or "4\u00D7 Platinum (RIAA)"@en or "431.0"^^<http://www.w3.org/2001/XMLSchema#double>


'''

menu_path = "G:\\xubo\\"
menu_path2 = "D:\\xubo\\dbpedia\\"
clean_infobox_file = open(menu_path2 + "clean_infobox.txt", 'w')
infobox_file = open(menu_path + "mappingbased_properties_en.nt", 'r')
infobox_lines = infobox_file.readlines()
for line in infobox_lines:
    try:
        line = line.rstrip()
        words = line.split(" ")
        if len(words) == 4:
    #     print line
            if words[0].startswith("<http://dbpedia.org/resource/") and words[1].startswith("<http://dbpedia.org/ontology/") and (words[2].startswith('"') or words[2].startswith("<http://dbpedia.org/resource/") ):
                entity = words[0][29:-1]
                attribute = words[1][29:-1]
                value = words[2]
                if value.startswith('"'):
#                     print value
                    value = value[value.find('"')+1:value.rfind('"')]
                else:
                    value = value[29:-1]
                
                
                
                clean_infobox_file.write("%s\t%s\t%s\n" %(entity, attribute, value))
            else:
                continue
    except:
        print "error: ", line