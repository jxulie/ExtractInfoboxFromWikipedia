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
# NEW_ARTICLE_MENU = "D:\\xubo\\ENwiki\\newdata2\\"
# test_file = open(NEW_ARTICLE_MENU + "1000.txt", 'r')
# test_lines = test_file.readlines()
# print len(test_lines)
# for line in test_lines:
#     print line.rstrip()
# 
# import nltk.data
# sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
# test_file = open("D:\\xubo\\ENwiki\\data3\\10.txt", 'r')
# write_file = open("D:\\xubo\\ENwiki\\data3\\20.txt", 'w')
# test_content = test_file.read()
# sentences = sent_detector.tokenize(test_content.strip())
# for sentence in sentences:
#     write_file.write(sentence + "\n")
# # print '\n-----\n'.join(sent_detector.tokenize(test_content.strip()))
# write_file.close()
# test_file.close()
# # import nltk
# nltk.download()

# import nltk
# sample_sentence = "united states. australia, Mr. xu said he loves me"
# # sentences = nltk.sent_tokenize(rawtext) # NLTK default sentence segmenter
# sentences = nltk.sent_tokenize(sample_sentence)
# print sentences
# sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
# tokens = nltk.word_tokenize(sample_sentence)
# print tokens
# sentences = [nltk.pos_tag(sent) for sent in sentences] # NLTK POS tagger
# tags = nltk.pos_tag(tokens)
# print tags

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
    print entity
#     for line in article_file.readlines():
#         print line
#         break
    article_content = article_file.read()
#     article_content = "".join(article_file.readlines())
#     print article_content[0:1000]
    article_sentences = sent_detector.tokenize(article_content.strip())
    article_sentence_num = len(article_sentences)
    if article_sentence_num > 1:
        article_sentence_file = open(NEW_ARTICLE_MENU + article, 'w')
        for i in range(0,article_sentence_num):
            article_sentence_file.write(article_sentences[i] + "\n")
        article_sentence_file.close()
        article_id_file.write("%s\t%s\n" %(entity, article))
article_id_file.close()