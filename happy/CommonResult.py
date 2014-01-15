#-*- coding:UTF-8 -*-
'''
Created on 2014年1月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

dict = {'ob1':'computer', 'ob2':'mouse', 'ob3':'printer'}  
'''
MENU_PATH = "D://xubo//ENwiki//sample//"
compare_path = MENU_PATH + "compare_infobox.txt"

result_dict = {'single-single-yes':0, 'single-single-no':0, 'single-multi-yes':0, 'single-multi-no':0,
               'multi-single-yes':0, 'multi-single-no':0, 'multi-multi-all':0, 'multi-multi-part':0,
               'multi-multi-no':0}

compare_file = open(compare_path, 'r')
compare_lines = compare_file.readlines()
for line in compare_lines:
    line = line.rstrip()
    words = line.split("\t")
    attribute1 = words[1].split("|")
    attribute2 = words[2].split("|")
    
    if len(attribute1) == 1 and len(attribute2) == 1:
        if attribute1[0] in attribute2[0] or attribute2[0] in attribute1[0]:
            result_dict['single-single-yes'] += 1
        else:
            result_dict['single-single-no'] += 1
            
    elif len(attribute1) == 1 and len(attribute2) > 1:
        flag = False
        for at in attribute2:
            if attribute1[0] in at or at in attribute1[0]:
                flag = True
                break
        if flag == True:
            result_dict['single-multi-yes'] += 1
        else:
            result_dict['single-multi-no'] += 1
            
    elif len(attribute1) > 1 and len(attribute2) == 1:
        flag = False
        for at in attribute1:
            if attribute2[0] in at or at in attribute2[0]:
                flag = True
                break
        if flag == True:
            result_dict['multi-single-yes'] += 1
        else:
            result_dict['multi-single-no'] += 1
    else:
        set1 = set(attribute1)
        set2 = set(attribute2)
        set3 = set1.union(set2)
        if len(set3) == len(set1) + len(set2):
            result_dict['multi-multi-no'] += 1
        elif len(set3) == len(set1) and len(set3) == len(set2):
            result_dict['multi-multi-all'] += 1
        else:
            result_dict['multi-multi-part'] += 1
compare_file.close()

for k, v in result_dict.iteritems():
    print k,"\t",v