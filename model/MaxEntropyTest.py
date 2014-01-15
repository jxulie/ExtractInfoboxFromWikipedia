#-*- coding:UTF-8 -*-
'''
Created on 2013年12月24日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Test the model

'''
import time
import nltk
from nltk.corpus import stopwords
import string
import pickle
class MaxEntropyTest(object):
    
    train_path = None
    model_path = None
    word_features = None
    pos_features = None
    stop = None
    
    def __init__(self, test_path, model_path, word_path, pos_path):
        self.test_path = test_path
        self.model_path = model_path
        self.stop = stopwords.words("english")
        self.load_features(word_path, pos_path)
        self.testing()
    

    
    def load_features(self, word_path, pos_path):
        self.word_features = list()
        self.pos_features = list()
        word_file = open(word_path, 'r')
        word_lines = word_file.readlines()
        for line in word_lines:
            line = line.rstrip()
            self.word_features.append("line")
        word_file.close()
        
        pos_file = open(pos_path, 'r')
        pos_lines = pos_file.readlines()
        for line in pos_lines:
            line = line.rstrip()
            self.pos_features.append("line")
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
    
    
    def testing(self):
        classifier = self.load_classifier()
        test_file = open(self.test_path, 'r')
        test_lines = test_file.readlines()
        for line in test_lines:
            line = line.rstrip()
            print classifier.classify(self.sentence_features(line)), line
        test_file.close()


    
    def load_classifier(self):
        f = open(self.model_path, 'rb')
        classifier = pickle.load(f)
        f.close
        return classifier

if __name__ == "__main__":
    MENU_PATH = "D://xubo//ENwiki//"
    TRAINING_PATH = MENU_PATH + "test_file.txt"
    MODEL_PATH = MENU_PATH + "maxent.pickle"
#     word_path, pos_path
    WORD_PATH = MENU_PATH + "word.pickle"
    POS_PATH = MENU_PATH  + "pos.pickle"
    STARTTIME = time.clock()
    TEST = MaxEntropyTest(TRAINING_PATH, MODEL_PATH, WORD_PATH, POS_PATH)
    ENDTIME = time.clock()
    print "last : ", ENDTIME - STARTTIME
    