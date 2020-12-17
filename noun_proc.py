# -*- coding: utf-8 -*- 

import numpy as np
import pandas as pd

from konlpy.tag import Okt
okt = Okt()

# from konlpy.tag import Mecab
# mecab = Mecab()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances

# for NAVER articles
def article_proc(article):
    art = article.split("▶")
    if len(art) > 1:
        icle = art[:-3]
        s = ""
        for t in icle:
            s += t
        article = s
    return article

# okt
def get_morphs(text):
    tags = okt.pos(text, norm='True', stem='True')
    l = [] 
    for words in tags:  
        l.append(words[0])
    return l

# #mecab
# def get_morphs(text):
#     tags = mecab.pos(text)
#     l = [] 
#     for words in tags:  
#         l.append(words[0])
#     return l

def nonset_jac_sim(article, text):
    article = get_morphs(article)
    comments = get_morphs(text)
    inter = []
    for comment in comments:
        if comment in article:
            inter.append(comment)
    uni = set(comments).union(set(article))
    return len(inter)/len(uni)

def tfid_vectorize(article, comment):
    sent = (article, comment)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sent) #문장 벡터화 진행
    return tfidf_matrix

def cos_sim(matrix):
    sim = cosine_similarity(matrix[0:1], matrix[1:2]) #첫번째와 두번째 문장 비교
    return sim[0][0]

def l1_normalize(v):
    norm = np.sum(v)
    return v / norm

def nor_euc_dis(matrix):
    tfidf_norm_l1 = l1_normalize(matrix)
    sim = euclidean_distances(tfidf_norm_l1[0:1], tfidf_norm_l1[1:2])
    return sim[0][0]

def list_calculate(l1, l2, k):
    if k == 0:
        l = l1
    elif k == 1:
        ldf = pd.DataFrame([l1]+[l2])
        ldf = ldf.T
        ldf[2] = ldf[0] + ldf[1]
        l =ldf[2].tolist()
    elif k == -1:
        ldf = pd.DataFrame([l1]+[l2])
        ldf = ldf.T
        ldf[2] = ldf[0] - ldf[1]
        l =ldf[2].tolist() 
    elif k == 2:
        ldf = pd.DataFrame([l1]+[l2])
        ldf = ldf.T
        ldf[2] = (ldf[0] * ldf[1])**(1/2)
        l =ldf[2].tolist()
    return l
