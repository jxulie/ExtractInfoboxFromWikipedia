#-*- coding:UTF-8 -*-
'''
Created on 2014年1月13日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''

import os

class SchemaValueSentence(object):
    '''Construct (category, attribute, value, sentence) training data
    Step1: read the schema entity value file.
    Step2: For each schema, find value sentences
    through entity-value and entity-sentence files
    '''
    article_id_dict = dict()
    def __init__(self, schema_entity_value_menu, \
                 article_id_path, article_menu, schema_value_sentence_menu):
        '''Notice that: schema_entity_value_menu is a menu, not a path'''
        if not os.path.exists(schema_value_sentence_menu):
            os.makedirs(schema_value_sentence_menu)
        self.read_article_id(article_id_path)
        self.read_schema_entity_value_file(schema_entity_value_menu, \
                                           article_menu, \
                                           schema_value_sentence_menu)


    def read_article_id(self, article_id_path):
        '''construct the correspond between article and id'''
        article_id_file = open(article_id_path, 'r')
        lines = article_id_file.readlines()
        for line in lines:
            line = line.rstrip()
            words = line.split("\t")
            self.article_id_dict[words[0]] = words[1]
        article_id_file.close()

    def read_schema_entity_value_file(self, \
                                      schema_entity_value_menu, \
                                      article_menu, \
                                      schema_value_sentence_menu):
        '''Step1: read the schema entity value file.'''
        schema_list = os.listdir(schema_entity_value_menu)
        for schema in schema_list:
            self.read_each_schema_file(schema_entity_value_menu, \
                                       schema, \
                                       article_menu, \
                                       schema_value_sentence_menu)

    def read_each_schema_file(self, \
                              schema_entity_value_menu, \
                              schema, \
                              article_menu, \
                              schema_value_sentence_menu):
        '''read each schema file'''
        try:
            match_file = open(schema_value_sentence_menu + schema, 'w')
            schema_file = open(schema_entity_value_menu + schema, 'r')
            schema_lines = schema_file.readlines()
            for line in schema_lines:
                line = line.rstrip()
                words = line.split("\t")
                error_id = 0
#                 print words[0] + "++++++++++++++" + words[1]
                try:
                    
                    article_lines = self.read_each_article_file(article_menu, \
                                                                words[0])
                    error_id += 1
                    if article_lines != None:
#                         print words[1]
                        best_sentence = self.find_best_sentence(words[1], article_lines)
                        if len(best_sentence) > 0:
                            for each_sentence in best_sentence:
                                match_file.write("%s\t%s\n" %(words[1], each_sentence))
#                         self.write_match_sentence(schema, \
#                                                  words[1], \
#                                                  article_lines, \
#                                                  schema_value_sentence_menu)
                    error_id += 1
                except IOError:
                    print "error_id is " + error_id
                    print article_menu + words[0] + ".txt" + "not exist"
            match_file.close()
            schema_file.close()
        except IOError:
            print schema + schema + " not exist"
    
    @staticmethod
    def find_best_sentence(value, lines):
        '''if any(word in 'some one long two phrase three' for word in aaa):
    print "right"'''
        tokens = value.split("|")
        best_sentence = list()
        for line in lines:
#             print line
            line = line.lower()
            if line.startswith("|") == False:
                line = line.rstrip()
                if any(token in line for token in tokens):
                    best_sentence.append(line)
        return best_sentence

    def read_each_article_file(self, article_menu, entity):
        '''read each article, and return the lines'''
        article_lines = None
        if entity in self.article_id_dict:
#             print entity, self.article_id_dict[entity], article_menu + self.article_id_dict[entity]
            article_file = open(article_menu + self.article_id_dict[entity], 'r')
            article_lines = article_file.readlines()
        return article_lines

#     @staticmethod
#     def write_match_sentence(schema, \
#                             value, \
#                             lines, \
#                             schema_value_sentence_menu):
#         '''find value in sentence of file
#         if value in sentence, write value,sentence pair'''
# 
#         match_file = open(schema_value_sentence_menu + schema, 'a')
#         for line in lines:
#             line = line.rstrip()
#             if value in line:
#                 if line.startswith("|") == False:
#                     match_file.write("%s\t%s\n" %(value, line))
#         match_file.close()

if __name__ == "__main__":
#     MENU_PATH = "D://xubo//ENwiki//"
#     SCHEMA_ENTITY_VALUE_MENU = MENU_PATH + "trainset1//"
#     SCHEMA_VALUE_SENTENCE_MENU = MENU_PATH + "trainset22//"
    MENU_PATH = "D://xubo//ENwiki//sample//"
    SCHEMA_ENTITY_VALUE_MENU = MENU_PATH + "newtrainset11//"
    SCHEMA_VALUE_SENTENCE_MENU = MENU_PATH + "newtrainset22//"
    
    MENU_PATH2 = "D://xubo//ENwiki//"
    ARTICLE_ID_PATH = MENU_PATH2 + "article_id"
    ARTICLE_MENU = MENU_PATH2 + "newdata//"
    TEST = SchemaValueSentence(SCHEMA_ENTITY_VALUE_MENU, \
                         ARTICLE_ID_PATH, \
                         ARTICLE_MENU, SCHEMA_VALUE_SENTENCE_MENU)
