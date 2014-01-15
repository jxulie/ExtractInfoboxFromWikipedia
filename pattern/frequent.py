#-*- coding:UTF-8 -*-
'''
Created on 2014年1月10日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 找到所有频繁出现的包含value的字串

第一步: 将所有value替换成一个不出现的词，如"jxulie"
第二步: 以"jxulie"为原点0，构建一个pos_tokenlist_dict。每个位置上存储一个tokenlist，设置阈值，过滤掉位置中出现次数较少的词
第三步：将所有位置中的频繁项集连接起来
第四步：找到所有候选的pattern
'''
import nltk
from collections import Counter

pos_tokenlist_dict = dict() #key:pos value:tokenlist
postoken_set_dict = dict() #key:pos,token value:sentence set

pattern_file = open("D://xubo//ENwiki//trainset22//new_artist", 'r')
print "hell"
pattern_lines = pattern_file.readlines()
sentence_count = 0
for line in pattern_lines:
    line = line.lower().rstrip()
    sentence_count += 1
#     print line
    words = line.split("\t")
    value = words[0]
    sentence = words[1]
    new_sen = sentence.replace(value, "jxulie")
    token_list = nltk.word_tokenize(new_sen)
    if "jxulie" in token_list:
        zero_pos = token_list.index("jxulie")
        for position, item in enumerate(token_list):
            new_position = position - zero_pos
            if new_position not in pos_tokenlist_dict:
#                 print position - zero_pos, item
                pos_tokenlist_dict[new_position] = list()
            pos_tokenlist_dict[new_position].append(item)
            if (new_position, item) not in postoken_set_dict:
                postoken_set_dict[(new_position, item)] = set()
            postoken_set_dict[(new_position, item)].add(sentence_count)

temp_tokens = dict()
result_tokens = dict()
for pos, tokenlist in pos_tokenlist_dict.iteritems():
#     frequent_token = Counter(tokenlist).most_common()
    filter_tokens = [k for k, v in Counter(tokenlist).iteritems() if v > 5 ]

    if len(filter_tokens) > 0:
        print pos, filter_tokens
# 0 ['jxulie']
# -2 ['time']
# -7 ['the']
# -4 ['a']
# -3 ['running', 'the']
# -1 ['of']
        temp_tokens[pos] = filter_tokens

left_pos = 0
#     left expand
while left_pos in temp_tokens:
    result_tokens[left_pos] = temp_tokens[left_pos]
    left_pos -= 1
right_pos = 0
#     left expand
while right_pos in temp_tokens:
    result_tokens[right_pos] = temp_tokens[right_pos]
    right_pos += 1

print sorted(result_tokens.iteritems())
# [(-4, ['a']), (-3, ['running', 'the']), (-2, ['time']), (-1, ['of']), (0, ['jxulie'])]