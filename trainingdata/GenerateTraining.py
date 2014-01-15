#-*- coding:UTF-8 -*-
'''
Created on 2013年12月23日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Generate Training Set

positive training from value sentence

negtive training from random.shuffle file list
'''
import os
import random

MENU_PATH = "D://xubo//ENwiki//"
ARTICLE_ID_PATH = MENU_PATH + "article_id"
ARTICLE_MENU = MENU_PATH + "newdata//"
SCHEMA_VALUE_SENTENCE_MENU = MENU_PATH + "trainset22//"

training_dict = dict()
schema_list = os.listdir(SCHEMA_VALUE_SENTENCE_MENU)
for schema in schema_list:
    schema_file = open(SCHEMA_VALUE_SENTENCE_MENU + schema, 'r')
    schema_lines = schema_file.readlines()
    for line in schema_lines:
        line = line.rstrip()
        words = line.split("\t")
        training_dict[words[1]] = schema
    schema_file.close()

# =====================================================================
train_file2 = open(MENU_PATH + "train_file2.txt", 'w')
for k2,v2 in training_dict.iteritems():
    train_file2.write("%s\t%s\n" %(k2, v2))
train_file2.close()
# =================================================================

entity_list = list()
sample_category_file = open("D://xubo//ENwiki//sample_category_final.txt", 'r')
sample_category_lines = sample_category_file.readlines()
for line in sample_category_lines:
    line = line.rstrip()
    words = line.split("\t")
    entity_list.append(words[0])
sample_category_file.close()

# =====================================================================
article_id_dict = dict()
article_id_file = open(ARTICLE_ID_PATH, 'r')
lines = article_id_file.readlines()
for line in lines:
    line = line.rstrip()
    words = line.split("\t")
    article_id_dict[words[0]] = words[1]
article_id_file.close()

# =====================================================================
count_num = 0
random.shuffle(entity_list)
for entity in entity_list:
    try:
        if count_num > 100:
            break
        entity_file = open(ARTICLE_MENU + article_id_dict[entity], 'r')
        entity_lines = entity_file.readlines()
        for line in entity_lines:
            line = line.rstrip()
            if line not in training_dict:
                training_dict[line] = "no_class"
        count_num += 1
    except:
        print entity, " is not exist"

# =====================================================================
train_file = open(MENU_PATH + "train_file.txt", 'w')
for k,v in training_dict.iteritems():
    train_file.write("%s\t%s\n" %(k, v))
train_file.close()