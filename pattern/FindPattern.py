#-*- coding:UTF-8 -*-
'''
Created on 2014年1月11日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Find Frequent Sub-String

'''
import time
import nltk
from collections import Counter

class FindPattern(object):
    
    train_path = None
    pattern_list = list()
    pattern_count_dict = dict()

    def __init__(self, train_path):
        self.train_path = train_path
        self.add_pattern()
        self.count_pattern()

    def add_pattern(self):
        pattern_file = open(self.train_path, 'r')
        pattern_lines = pattern_file.readlines()
        for line in pattern_lines:
            pattern_set = set()
            line = line.lower().rstrip()
            words = line.split("\t")
            value = words[0]
            sentence = words[1]
            new_sen = sentence.replace(value, "jxulie")
            token_list = nltk.word_tokenize(new_sen)
            if "jxulie" in token_list:
#                 print line
                zero_pos = token_list.index("jxulie")
#                 print zero_pos
                total_len = len(token_list)
                for i in range(0, zero_pos):
                    for j in range(zero_pos, total_len):
#                         print token_list[i:j+1]
                        token_string = " ".join(token_list[i:j+1])
#                         print token_string
#                         self.pattern_list.append((len(token_list[i:j+1]),token_string))
                        pattern_set.add((len(token_list[i:j+1]),token_string, value))
            for pa in pattern_set:
                self.pattern_list.append(pa)

    def count_pattern(self):
        perfect_pattern = list()
        for pattern_len, pattern, entity in self.pattern_list:
#             pattern_len =  len(pattern)
            if (pattern_len, pattern) not in self.pattern_count_dict:
                self.pattern_count_dict[(pattern_len, pattern)] = set()
            self.pattern_count_dict[(pattern_len, pattern)].add(entity)

        for key, value in sorted(self.pattern_count_dict.iteritems(), key = lambda k: k[0], reverse = True):
            if len(value) > 15 and key[0] > 3:
                flag = False
                for length, pattern, count in perfect_pattern:
                    if key[1] in pattern:
                        flag = True
                        break
                if flag == False:
                    perfect_pattern.append((key[0], key[1], len(value)))
        
        for pe in perfect_pattern:
            print pe
                                         
if __name__ == "__main__":
    MENU_PATH = "D://xubo//ENwiki//sample"
    TRAINING_PATH = MENU_PATH + "//newtrainset22//new_artist"
#     TRAINING_PATH = MENU_PATH + "//trainset22//test.txt"
    STARTTIME = time.clock()
    TEST = FindPattern(TRAINING_PATH)
    ENDTIME = time.clock()
    print "last : ", ENDTIME - STARTTIME