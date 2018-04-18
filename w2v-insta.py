# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:13:17 2018

@author: sangil
"""
import json
from konlpy.tag import Twitter
from gensim.models import word2vec


# 유저당 태그를 스트링 리스트로 나타냄
def bfr_taeso(filename):
    bfr_taeso = []
    with open(filename, encoding="utf-8") as data_file:
        data = json.load(data_file)
    for i in data:
        bfr_taeso.append(i['content'])
    return bfr_taeso


# 유저당 태그를 스트링으로 합치기
def getFullString(list):
    temp_nouns = []
    str_temp = ''
    for tags in list:
        tags = tags.replace('\n', '')
        tags = tags.split(' ')
        for tag in tags:
            if '#' in tag:
                temp_nouns.append(tag.split('#'))
    for v in temp_nouns:
        str_temp += v[1]
    return str_temp


# 합친 스트링에서 필요한 품사만 추출하고 tagdata라는 파일로 저장하기
def getTaeso(str):
    twitter = Twitter()
    pumsas = twitter.pos(str)
    # useful=[n for n, pumsa in pumsas if pumsa =='Noun'or 'Verb']
    # with open("tagdata", "w", encoding='utf-8') as fp:
    #    fp.write(useful)
    return pumsas


# getTaeso(getFullString(bfr_taeso('mangridan.json')))
# str =getFullString(bfr_taeso('mangridan.json'))
# getTaeso(str)

# word2vec 실행
data = word2vec.LineSentence("tagdata")
model = word2vec.Word2Vec(data, size=20, window=10, min_count=2, hs=1, sg=1)
model.save("w2v.result")


# 유저당 태그라인과 10개의 외식업들 간의 상관도를 비교하여 높은 상관도를 보이는 외식업 종류를
# 태그라인의 외식업 종류라고 분류한다.
def analysis(filename):
    model = word2vec.Word2Vec.load(filename)
    sign1 = model.wv['짜장면']  # 중국식
    sign2 = model.wv['떡볶이']  # 분식집
    sign3 = model.wv['밥']  # 한식
    sign4 = model.wv['초밥']  # 일식
    sign5 = model.wv['파스타']  # 양식
    sign6 = model.wv['햄버거']  # 패스트푸트점
    sign7 = model.wv['칵테일']  # 호프/간이주점
    sign8 = model.wv['카페']  # 카페
    sign9 = model.wv['빵']  # 제과점
    sign10 = model.wv['치킨']  # 치킨전문점
    total_sign = [sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9, sign10]

def get_redundant_pairs(df):
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

print("Top Absolute Correlations")
print(get_top_abs_correlations(df, 3))