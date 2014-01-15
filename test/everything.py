#-*- coding:UTF-8 -*-
'''
Created on 2013年12月15日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: Test everything

'''
# import re
# refile = open("D://xubo//ENwiki//test//refine.txt", 'w')
# infofile = open("D://xubo//ENwiki//sample_infobox_final2.txt", 'r')
# infolines = infofile.readlines()
# for line in infolines:
#     value_list = list()
#     line = line.rstrip()
#     words = line.split("\t")
# #     re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr);
#     words[2] = re.sub(r"\(\s+\)", "", words[2])
#     tokens = words[2].replace("jxulie", "\t").replace("[[", "\t").replace("]]", "\t")
#     values = tokens.split("\t")
#     for value in values:
#         value = value.strip()
#         if value != "":
#             if value.find("|") != -1:
#                 value = value[value.find("|")+1:]
#             if value != "" and value.find("''")== -1 and value.find("(")== -1:
#                 value_list.append(value)
#     if len(value_list) > 0:
#         refile.write("%s\t%s\t%s\n" %(words[0],words[1],"|".join(value_list)))
# refile.close()
     


# aaa = "bruce lee [[john saxon (actor)|john saxon]] [[jim kelly (martial artist)|jim kelly]] paul green {{small|(uncredited)}} [[ahna capri]] [[shih kien]] [[robert wall]] carl lerner [[gerda lerner]] "
# aaa = re.sub(r"\{\{[\s\S]+\}\}", "", aaa)
# aaa = re.sub(r"\([\s\S]+\)", "", aaa)
# bbb = aaa.replace("jxulie", "\t").replace("[[", "\t").replace("]]", "\t")
# ccc = bbb.split("\t")
# for c in ccc:
#     c = c.strip()
# #     c = re.sub(r"\{\{[\s\S]+\}\}", "", c)
# #     c = re.sub(r"\([\s\S]+\)", "", c)
#     if c != "":
#         if c.find("|") != -1:
#             c = c[c.find("|")+1:]
#         print c

# aaa = ", ,aab}}"
# aaa= aaa.strip(" ,}")
# print aaa

# aaa = "because you're mine    103 minutes"
# bbb = "some one long two 10"
# print bbb
# ccc = bbb.split(" ")
# print ccc
# if any(word in aaa for word in ccc):
#     print "right"

# from nltk.corpus import names
# import nltk
# import random
# def gender_features(word):
#     return {'last_letter': word[-1]}
#   
#      
# def gender_features2(name):
#     features = {}
#     features["firstletter"] = name[0].lower()
#     features["lastletter"] = name[-1].lower()
#     for letter in 'abcdefghijklmnopqrstuvwxyz':
#         features["count(%s)" % letter] = name.lower().count(letter)
#         features["has(%s)" % letter] = (letter in name.lower())
#     return features
#   
# names = ([(name, 'male') for name in names.words('male.txt')] +
#             [(name, 'female') for name in names.words('female.txt')])
#   
# print names[0]
# # print random.shuffle(names)
# featuresets = [(gender_features2(n), g) for (n,g) in names]
# train_set, test_set = featuresets[500:], featuresets[:500]
# classifier2 = nltk.maxent.train_maxent_classifier_with_scipy(train_toks = train_set, algorithm = "LBFGSB")
# # classifier = nltk.NaiveBayesClassifier.train(train_set)
# print classifier2.classify(gender_features2('xubo'))
# # print classifier.show_most_informative_features(10)

# from nltk.corpus import movie_reviews
# import nltk
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# for word in all_words[0:2000]:
#     print word,all_words.freq(word)

# 
# import nltk
# 
# 
#      
# train = [
# (dict(a=1,b=1,c=1), 'y'),
# (dict(a=1,b=1,c=1), 'x'),
# (dict(a=1,b=1,c=0), 'y'),
# (dict(a=0,b=1,c=1), 'x'),
# (dict(a=0,b=1,c=1), 'y'),
# (dict(a=0,b=0,c=1), 'y'),
# (dict(a=0,b=1,c=0), 'x'),
# (dict(a=0,b=0,c=0), 'x'),
# (dict(a=0,b=1,c=1), 'y'),
# ]
# 
# test = [
# (dict(a=1,b=0,c=1)), # unseen
# (dict(a=1,b=0,c=0)), # unseen
# (dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
# (dict(a=0,b=1,c=0)), # seen 1 time, label=x
# ]
# 
# algorithm = nltk.classify.MaxentClassifier.ALGORITHMS[0]
# print algorithm
# classifier = nltk.MaxentClassifier.train(train, "GIS")
# print classifier.batch_classify(test)
# def test_maxent(algorithms):
#     classifiers = {}
#     for algorithm in nltk.classify.MaxentClassifier.ALGORITHMS:
#         if algorithm.lower() == 'megam':
#             try: nltk.classify.megam.config_megam()
#             except: raise #continue
#             try:
#                 classifiers[algorithm] = nltk.MaxentClassifier.train(train, algorithm, trace=0, max_iter=1000)
#             except Exception, e:
#                 classifiers[algorithm] = e
#                 print ' '*11+''.join(['      test[%s]  ' % i
#                                       for i in range(len(test))])
#                 print ' '*11+'     p(x)  p(y)'*len(test)
#                 print '-'*(11+15*len(test))
#                 for algorithm, classifier in classifiers.items():
#                     print '%11s' % algorithm,
#                     if isinstance(classifier, Exception):
#                         print 'Error: %r' % classifier; continue
#                         for featureset in test:
#                             pdist = classifier.prob_classify(featureset)
#                             print '%8.2f%6.2f' % (pdist.prob('x'), pdist.prob('y')),
#                             print
# test_maxent(nltk.classify.MaxentClassifier.ALGORITHMS)
# import random
# p = ["Python", "is", "powerful", "simple", "and so on..."]  
# random.shuffle(p)  
# print p
# import nltk
# aaa = "aaa bbb cdd sss sss aaa bbb"
# all_words = nltk.FreqDist(w for w in aaa.split(" "))
# print all_words
# word_features = all_words.keys()[:2000]
# print word_features
# import nltk
# from nltk.corpus import stopwords
# import string
# 
# aaa = "i am a big boy, in a big city"
# 
# 
# stop = stopwords.words("english")
# # print stop
# # bbb = set(token for token in nltk.word_tokenize(aaa) if token not in stop and token not in string.punctuation)
# # print bbb
# tokens = [token for token in nltk.word_tokenize(aaa) if token not in stop and token not in string.punctuation]
# print "i" in tokens
# pos = nltk.pos_tag(tokens)
# print tokens
# print [i[1] for i in pos]
# all_words = nltk.FreqDist(tokens)
# all_pos = nltk.FreqDist(pos)
# 
# print all_words
# print all_pos
# 
# for k,v in all_words.iteritems():
#     print k, v



import nltk
import pickle
train = [
(dict(a=1,b=1,c=1), 'y'),
(dict(a=1,b=1,c=1), 'x'),
(dict(a=1,b=1,c=0), 'y'),
(dict(a=0,b=1,c=1), 'x'),
(dict(a=0,b=1,c=1), 'y'),
(dict(a=0,b=0,c=1), 'y'),
(dict(a=0,b=1,c=0), 'x'),
(dict(a=0,b=0,c=0), 'x'),
(dict(a=0,b=1,c=1), 'y'),
]
 
test = [
(dict(a=1,b=0,c=1)), # unseen
(dict(a=1,b=0,c=0)), # unseen
(dict(a=0,b=1,c=1)), # seen 3 times, labels=y,y,x
(dict(a=0,b=1,c=0)), # seen 1 time, label=x
]


def save_classifier(classifier):
    f = open('my_classifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()


def load_classifier():
    f = open('my_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close
    return classifier

classifier = nltk.MaxentClassifier.train(train, "GIS")
save_classifier(classifier)
classifier2 = load_classifier()
for data in test:
    result = classifier2.classify(data)
    print data, result
# print classifier.batch_classify(test)
# print classifier2.batch_classify(test)