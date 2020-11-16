#!/usr/bin/env python
# coding: utf-8

#get_ipython().system('pip install konlpy')
#get_ipython().system('pip install newspaper3k')
from konlpy.tag import Kkma
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np

def newsfromtext(filename):
    f = open(filename, 'r', encoding='utf-8')
    news_body = f.read()
    return news_body

def sent_tokenize(text):
    kkma = Kkma()
    result = kkma.sentences(text)
    return result

def noun_extract(sentences):
    okt = Okt()
    result = []
    for s in sentences:
        result.append(' '.join([w for w in okt.nouns(str(s))]))
    return result

class GraphMatrix(object):
    def __init__(self):
        self.tfidf = TfidfVectorizer()
        self.cnt_vec = CountVectorizer()
        self.graph_sentence = []
        
    def build_sent_graph(self, sentence):
        tfidf_mat = self.tfidf.fit_transform(sentence).toarray()
        self.graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
        return self.graph_sentence
    
    def build_words_graph(self, sentence):
        cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
        vocab = self.cnt_vec.vocabulary_
        return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}

class Rank(object):
    def get_ranks(self, graph, d=0.85): # d = damping factor
        A = graph
        matrix_size = A.shape[0]
        for id in range(matrix_size):
            A[id, id] = 0 # diagonal 부분을 0으로
            link_sum = np.sum(A[:,id]) # A[:, id] = A[:][id]
            if link_sum != 0:
                A[:, id] /= link_sum
            A[:, id] *= -d
            A[id, id] = 1
        
        B = (1-d) * np.ones((matrix_size, 1))
        ranks = np.linalg.solve(A, B) # 연립방정식 Ax = b
        return {idx: r[0] for idx, r in enumerate(ranks)}

class TextRank(object):
    def __init__(self, text):
        self.sentences = sent_tokenize(text)
        self.nouns = noun_extract(self.sentences)
        
        self.graph_matrix = GraphMatrix()
        self.sent_graph = self.graph_matrix.build_sent_graph(self.nouns)
        
        self.words_graph, self.idx2word = self.graph_matrix.build_words_graph(self.nouns)
        self.rank = Rank()
        self.sent_rank_idx = self.rank.get_ranks(self.sent_graph)
        self.sorted_sent_rank_idx = sorted(self.sent_rank_idx, key=lambda k: self.sent_rank_idx[k], reverse=True)
        self.word_rank_idx = self.rank.get_ranks(self.words_graph)
        self.sorted_word_rank_idx = sorted(self.word_rank_idx, key=lambda k: self.word_rank_idx[k], reverse=True)

    def keywords(self, word_num=10):
        rank = Rank()
        rank_idx = rank.get_ranks(self.words_graph)
        sorted_rank_idx = sorted(rank_idx, key=lambda k: rank_idx[k], reverse=True)
        keywords = []
        index=[]
        for idx in sorted_rank_idx[:word_num]:
            index.append(idx)
        index.sort()
        for idx in index:
            keywords.append(self.idx2word[idx])
        return keywords

#test = '트럼프가 주장한 부정선거랑 이번 우리나라 부정선거건은 아주 자연스럽게 연결될거 같네... ㅋㅋㅋㅋ... 재미있는 드라마 시작한다~~~~'
#print(test)
news_body = newsfromtext('news_body.txt')
#nnews = newsfromtext('news_3.txt')
#print(news)

abcd = TextRank(news_body)
print(abcd.keywords())

## TEST TEST TEST TEST TEST
#okt = Okt()
#print(okt.nouns(test))
#print(okt.nouns(news_body))
#sents = sent_tokenize(news_body)
#print(sents)
#nss = noun_extract(sents)
#print(nss)