#-*- coding:UTF-8 -*-
'''
Created on 2013年12月4日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Construct (category, attribute, value, sentence) training data

@version: 2.0

@summary: 从处理中文变成处理英文，增加article_id文件，即英文实体与ID的对应关系
                          主要是因为英文实体中存在冒号等不能作为文件名


input:

    schema entity value: (category, attribute, entity, value) split with "\t"
                        different schema(category, attribute) in different files

    article text:   text in Baidu Baike. split to sentences. each each a file

output:

    schema value sentence: (category, attribute, value, sentence)
                            split with "\t"
                        different schema(category, attribute) in different files
e.g.:

    schema entity value file

              歌手_经纪公司.txt
                 陈紫函    华谊兄弟传媒集团
                娄译心    索卡尼娱乐
                妮琪·米娜    YoungMoney/CashMoney/环球
                川澄绫子    大泽事务所
                范玮琪    百娱传媒股份有限公司
                胡蓓蔚    “永星”唱片公司
                超新星_(韩国组合)    CoreContentsMedia
                易灵汐    巧思传媒文化公司
                黄铠晴    东亚娱乐
                朴灿烈    SMEntertainment
                梁咏琪    美亚娱乐资讯集团有限公司
                雷·查尔斯    AtlanticRecords
                艾莉莎    喜乐音乐文化传媒（北京）公司
                练正华    成都歌舞剧院
                郑华娟    滚石唱片有限公司
                言承旭    戏梦堂娱乐经纪有限公司
    --end--

    article text
            陈紫函.txt

            籍贯陈紫函(6张)：重庆[1-3]
            中学：重庆南开中学
            大学：北京电影学院表演系
            家庭成员：父母、本人
            粉丝昵称：紫菜
            语言：中文、粤语、英语
            方言：重庆话
            特长：舞蹈、绘画、设计、单眼转
            爱好：阅读、旅行、保龄球
            宗教信仰陈紫函签名照(5张)：基督教
            宠物：卡卡、宝宝（雪纳瑞犬）、卢比（泰迪）
            最喜欢的水果：山竹
            最喜欢的糖果：巧克力
            最喜欢的食物：辣椒
            电视剧剧照(35张)最喜欢的颜色：蓝色、紫色
            最喜欢的衣着：休闲
            最喜欢的电影：《魂断蓝桥》
            最喜欢的男演员：反町隆史
            最喜欢的女演员：张曼玉
    --end--

    schema value sentence

            歌手_经纪公司.txt(different menu)
            华谊兄弟传媒集团    经纪公司是华谊兄弟传媒集团
    --end--

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
                                match_file.write("%s\t%s\n" %(words[1], best_sentence[0]))
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
    SCHEMA_ENTITY_VALUE_MENU = MENU_PATH + "newtrainset1//"
    SCHEMA_VALUE_SENTENCE_MENU = MENU_PATH + "newtrainset2//"
    
    MENU_PATH2 = "D://xubo//ENwiki//"
    ARTICLE_ID_PATH = MENU_PATH2 + "article_id"
    ARTICLE_MENU = MENU_PATH2 + "newdata//"
    TEST = SchemaValueSentence(SCHEMA_ENTITY_VALUE_MENU, \
                         ARTICLE_ID_PATH, \
                         ARTICLE_MENU, SCHEMA_VALUE_SENTENCE_MENU)
