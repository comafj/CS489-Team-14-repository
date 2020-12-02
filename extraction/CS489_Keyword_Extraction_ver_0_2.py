from konlpy.tag import Kkma
from konlpy.tag import Okt
from konlpy.tag import Mecab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np

# 현재는 news 내용만을 가지고 있는 txt파일을 여는 형식으로 구현되어 있으나
# crawling의 결과로 얻어지는 tsv 파일에서 얻는 형식으로 구현해야 한다
def newsfromtext(filename):
    f = open(filename, 'r', encoding='utf-8')
    news_body = f.read()
    f.close()
    return news_body

# Kkma를 이용해 sentence 별로 tokenize하여 바환
def sent_tokenize(text):
    kkma = Kkma()
    result = kkma.sentences(text)
    return result

# Okt를 이용해 각 문장들을 명사만 추출한 리스트로 바꾸어 반환
def noun_extract(sentences):
    okt = Okt()
    #mecab = Mecab()
    result = []
    for s in sentences:
        result.append(' '.join([w for w in okt.nouns(str(s))]))
    return result

# 단어들 사이의 GraphMatrix 정의를 위한 class
class GraphMatrix(object):
    def __init__(self):
        self.tfidf = TfidfVectorizer()
        self.cnt_vec = CountVectorizer()
        self.graph_sentence = []

    def build_words_graph(self, sentence):
        cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
        vocab = self.cnt_vec.vocabulary_
        return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}

# 요소별 Ranking을 얻기 위한 class
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

# 위에서 정의한 GraphMatrix와 Rank class를 통해 TextRank로 중요 단어 파악
class TextRank(object):
    def __init__(self, text):
        self.sentences = sent_tokenize(text)
        self.nouns = noun_extract(self.sentences)

        self.graph_matrix = GraphMatrix()
        self.words_graph, self.idx2word = self.graph_matrix.build_words_graph(self.nouns)
        self.rank = Rank()

        self.word_rank_idx = self.rank.get_ranks(self.words_graph)
        self.sorted_word_rank_idx = sorted(self.word_rank_idx, key=lambda k: self.word_rank_idx[k], reverse=True)

    def keywords(self, word_num):
        rank = Rank()
        rank_idx = rank.get_ranks(self.words_graph)
        sorted_rank_idx = sorted(rank_idx, key=lambda k: rank_idx[k], reverse=True)

        max_rank = rank_idx[sorted_rank_idx[0]]
        keywords = {}
        index=[]
        if word_num > 0:
            for idx in sorted_rank_idx[:word_num]:
                index.append(idx)
        else:
            for idx in sorted_rank_idx:
                index.append(idx)
        #index.sort()
        for idx in index:
            keywords[self.idx2word[idx]] = rank_idx[idx] / max_rank
        return keywords

# If word_num value is set as 0 or none, all of the noun scores will return
# Else if word_num value is some positive integer, only top of the noun scores will return
def keyfrombody(body, word_num=0):
    body_rank = TextRank(body)
    return body_rank.keywords(word_num)

def getcomments(filename):
    result = []
    f = open(filename, 'r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break
        result.append(line)
    f.close()
    return result

def keyword_analysis(keydict, comment_file):
    okt = Okt()
    #mecab = Mecab()
    sentence_score = []
    comments = getcomments(comment_file)
    for com in comments:
        score = 0
        com_noun = okt.nouns(com)
        for sn in com_noun:
            if sn in keydict: # If comment has some important keyword in body_text
                score += keydict[sn] # Accumulate its score
        sentence_score.append((com, score))
    return sentence_score

def new_ka(keydict, comments_str):
    okt = Okt()
    #mecab = Mecab()
    sentence_score = []
    index = 1
    for com in comments_str:
        score = 0
        com_noun = okt.nouns(com)
        for sn in com_noun:
            if sn in keydict:
                score += keydict[sn]
        sentence_score.append((index, score, com))
        index+=1
    return sentence_score

#score_test = keyword_analysis("news_body.txt", "comment_test.txt")
#c = getcomments("comment_test.txt")
#for i in range(len(c)):
#    print((c[i], score_test[i]))

#news_body = newsfromtext('news_2.txt')
#key_from_body = keyfrombody(news_body)
#print(key_from_body)
#comments = getcomments("comment_test.txt")
#print(comments[0])



## TEST TEST TEST TEST TEST
#okt = Okt()
#print(okt.nouns(test))
#print(okt.nouns(news_body))
#sents = sent_tokenize(news_body)
#print(sents)
#nss = noun_extract(sents)
#print(nss)
