#-*- coding:UTF-8 -*-
'''
Created on 2013年12月23日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Split multi value of infobox

aaa = "bruce lee [[john saxon (actor)|john saxon]] [[jim kelly (martial artist)|jim kelly]] paul green {{small|(uncredited)}} [[ahna capri]] [[shih kien]] [[robert wall]] carl lerner [[gerda lerner]] "
aaa = re.sub(r"\{\{[\s\S]+\}\}", "", aaa)
aaa = re.sub(r"\([\s\S]+\)", "", aaa)
bbb = aaa.replace("jxulie", "\t").replace("[[", "\t").replace("]]", "\t")
ccc = bbb.split("\t")
for c in ccc:
    c = c.strip()
#     c = re.sub(r"\{\{[\s\S]+\}\}", "", c)
#     c = re.sub(r"\([\s\S]+\)", "", c)
    if c != "":
        if c.find("|") != -1:
            c = c[c.find("|")+1:]
        print c

规则：
整个value一起处理
1. 去除包含 {{****}}的字符串
2. 去除包含(***)的字符串
3. 替换 &nbsp;、jxulie、[[、]]为\t
分割后
1. 过滤掉仅为空格的value
2. 找到锚文件，即包含“|”的，取后半部分
3. 过滤掉包含‘’以及为空的value
4. 去除头包含" " "," "{" "}" "."

@version: 2.0
分割后
5. 去除仅为and, with, / , &, ;的字段

'''
import re
# refile = open("D://xubo//ENwiki//sample_infobox_split_produced.txt", 'w')
# infofile = open("D://xubo//ENwiki//sample_infobox_produced.txt", 'r')
refile = open("D://xubo//ENwiki//origin//new_infobox_split.txt", 'w')
infofile = open("D://xubo//ENwiki//origin//new_infobox.txt", 'r')
infolines = infofile.readlines()
for line in infolines:
    try:
        value_list = list()
        line = line.rstrip()
        words = line.split("\t")
        valueset = words[2]
        valueset = re.sub(r"\{\{[\s\S]+\}\}", "", valueset)
        valueset = re.sub(r"\([\s\S]+\)", "", valueset)
        tokens = valueset.replace("&nbsp;"," ").replace("jxulie", "\t").replace("[[", "\t").replace("]]", "\t")
        values = tokens.split("\t")
        for value in values:
            value = value.strip(" ,{}().")
            if value != "":
                if value.find("|") != -1:
                    value = value[value.find("|")+1:]
                    value = value.strip(" ,{}().")
                if value != "" and value.find("''") and value.find('"')== -1:
                # @version: 2.0
                # 5. 去除仅为and, with, / , &的字段
                    if value not in ["and", "with", "/", "&", ";"]:
                        value_list.append(value)
        if len(value_list) > 0:
            refile.write("%s\t%s\t%s\n" %(words[0],words[1],"|".join(value_list)))
    except:
        print line
refile.close()
infofile.close()
