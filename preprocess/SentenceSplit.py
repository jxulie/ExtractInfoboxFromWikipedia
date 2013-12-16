#-*- coding:UTF-8 -*-
'''
Created on 2013年12月15日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Split text to sentences

'''
import os
ARTICLE_MENU = "D:\\xubo\\ENwiki\\data\\"
NEW_ARTICLE_MENU = "D:\\xubo\\ENwiki\\newdata\\"
ARTICLE_ID_PATH = "D:\\xubo\\ENwiki\\article_id"
if not os.path.exists(NEW_ARTICLE_MENU):
    os.makedirs(NEW_ARTICLE_MENU)
article_id_file = open(ARTICLE_ID_PATH, 'w')
article_list = os.listdir(ARTICLE_MENU)
count = 0
for article in article_list:
    count += 1
    if count%1000 == 0:
        print count
    article_file = open(ARTICLE_MENU + article, 'r')
    article_lines = article_file.readlines()
    article_sentences = list()
    for line in article_lines:
        line = line.strip()
        words = line.split(".")
        for word in words:
#             print word
            word = word.lstrip()
#             print word
            article_sentences.append(word)
    article_file.close()
    article_sentence_num = len(article_sentences)
    if article_sentence_num > 1:
        entity = article_sentences[0]
        article_sentence_file = open(NEW_ARTICLE_MENU + article, 'w')
        for i in range(1,article_sentence_num):
            article_sentence_file.write(article_sentences[i] + "\n")
        article_sentence_file.close()
        article_id_file.write("%s\t%s\n" %(entity, article))
article_id_file.close()
