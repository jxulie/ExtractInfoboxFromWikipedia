#-*- coding:UTF-8 -*-
'''
Created on 2013年12月23日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: maximum entropy model 

策略：
1.统计句子中的每个单词
2.统计句子中的每个单词的pos
3.需要去除stopword

input:

    training data:  sentence \t class \n

output:

    model pickle:  save the classifier

'''


import time
import nltk
from nltk.corpus import stopwords
import string
import pickle
class MaxEntropyModel(object):
    
    train_path = None
    model_path = None
    word_features = None
    pos_features = None
    stop = None
    
    def __init__(self, train_path, model_path, word_path, pos_path):
        self.train_path = train_path
        self.model_path = model_path
        self.stop = stopwords.words("english")
        self.prepare_features()
        self.write_features(word_path, pos_path)
#         self.training()
    
    def find_word_pos_list(self):
        word_list = list()
        pos_list = list()
        train_file = open(self.train_path, 'r')
        train_lines = train_file.readlines()
        for line in train_lines:
            line = line.rstrip()
            words = line.split("\t")
            sentence = words[0]
            word_freq = [token for token in nltk.word_tokenize(sentence) if token not in self.stop and token not in string.punctuation]
        #     word_freq = nltk.word_tokenize(sentence)
            pos_tuple_list = nltk.pos_tag(word_freq)
            pos_freq = [pos[1] for pos in pos_tuple_list]
            word_list.extend(word_freq)
            pos_list.extend(pos_freq)
        train_file.close()
        return (word_list, pos_list)
    
    @staticmethod
    def filter_freq(freq_dict, threshold):
        filter_set = set()
        for k, v in freq_dict.iteritems():
            if v < threshold:
                break
            filter_set.add(k)
        return filter_set

    def prepare_features(self):
        WORD_NUM_THRESHOLD = 10
        (word_list, pos_list) = self.find_word_pos_list()
        all_words = nltk.FreqDist(word_list)
        all_pos = nltk.FreqDist(pos_list)
        self.word_features = self.filter_freq(all_words, WORD_NUM_THRESHOLD)
        self.pos_features = self.filter_freq(all_pos, WORD_NUM_THRESHOLD)
    
    def write_features(self, word_path, pos_path):
        word_file = open(word_path, 'w')
        for word in self.word_features:
            word_file.write(word + "\n")
        word_file.close()
        
        pos_file = open(pos_path, 'w')
        for pos in self.pos_features:
            pos_file.write(pos + "\n")
        pos_file.close()

    def sentence_features(self, sentence):
        features = dict()
        word_freq = [token for token in nltk.word_tokenize(sentence) if token not in self.stop and token not in string.punctuation]
        pos_tuple_list = nltk.pos_tag(word_freq)
        pos_freq = [pos[1] for pos in pos_tuple_list]
        for word in self.word_features:
            features['contains(%s)' % word] = (word in word_freq)
        for pos in self.pos_features:
            features['haspos(%s)' % pos] = (pos in pos_freq)
        return features
    
    def training(self):
        train_data_list = list()
        train_file = open(self.train_path, 'r')
        train_lines = train_file.readlines()
        for line in train_lines:
            line = line.rstrip()
            words = line.split("\t")
            sentence = words[0]
            category = words[1]
            train_data_list.append((self.sentence_features(sentence), category))
        train_file.close()
        classifier = nltk.MaxentClassifier.train(train_data_list, "GIS")
        self.save_classifier(classifier)

    def save_classifier(self, classifier):
        f = open(self.model_path, 'wb')
        pickle.dump(classifier, f)
        f.close()
    
#     def load_classifier(self):
#         f = open('my_classifier.pickle', 'rb')
#         classifier = pickle.load(f)
#         f.close
#         return classifier

if __name__ == "__main__":
    MENU_PATH = "D://xubo//ENwiki//"
    TRAINING_PATH = MENU_PATH + "train_file2.txt"
    MODEL_PATH = MENU_PATH + "maxent.pickle"
#     word_path, pos_path
    WORD_PATH = MENU_PATH + "word.pickle"
    POS_PATH = MENU_PATH  + "pos.pickle"
    STARTTIME = time.clock()
    TEST = MaxEntropyModel(TRAINING_PATH, MODEL_PATH, WORD_PATH, POS_PATH)
    ENDTIME = time.clock()
    print "last : ", ENDTIME - STARTTIME
    