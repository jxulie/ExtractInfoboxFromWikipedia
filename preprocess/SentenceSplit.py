#-*- coding:UTF-8 -*-
'''
Created on 2013年12月15日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Split text to sentences

@version: 1.1

@summary: 修改bug, （1）增加一行 entity = file.readline()
                            由于第一行为entity，按nltk分段的情况会导致第一行不会被分为一行
                          因此，先用file.readline()读取第一行，再把其他的行一起读取file.read()
        (2)改为for i in range(0, article_sentence_num)。将1改为0，原因同上 

example:
import nltk.data
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
test_file = open("D:\\xubo\\ENwiki\\data3\\10.txt", 'r')
write_file = open("D:\\xubo\\ENwiki\\data3\\20.txt", 'w')
test_content = test_file.read()
sentences = sent_detector.tokenize(test_content.strip())
for sentence in sentences:
    write_file.write(sentence + "\n")
'''
import nltk.data
import os
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
ARTICLE_MENU = "D:\\xubo\\ENwiki\\data3\\"
NEW_ARTICLE_MENU = "D:\\xubo\\ENwiki\\newdata3\\"
ARTICLE_ID_PATH = "D:\\xubo\\ENwiki\\article_id3"
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
    entity = article_file.readline().rstrip()
    article_content = "".join(article_file.readlines())
    article_sentences = sent_detector.tokenize(article_content.strip())
    article_sentence_num = len(article_sentences)
    if article_sentence_num > 1:
        article_sentence_file = open(NEW_ARTICLE_MENU + article, 'w')
        for i in range(0, article_sentence_num):
            article_sentence_file.write(article_sentences[i] + "\n")
        article_sentence_file.close()
        article_id_file.write("%s\t%s\n" %(entity, article))
article_id_file.close()
