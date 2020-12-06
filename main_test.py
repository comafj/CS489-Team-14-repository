# In[]:

from crawling import crawl as cr
import utilfunc as ut

# -*- coding: utf-8 -*- 

import numpy as np

from konlpy.tag import Okt
okt = Okt()

from konlpy.tag import Mecab
mecab = Mecab()

import pandas as pd

# n = input("typing the number of tsv file: ")
n = "0"

dataset = pd.read_csv("/Users/bobopack/Downloads/CS489-Team-14-repository-main 3/crawling_output/crawling_output_{0}.tsv".format(n)
, delimiter='\t', names = ['제목/댓글번호','기사작성시간/댓글본문','기사본문/좋아요','none/싫어요','none/답글수'])

datatable = dataset.values.tolist()


title = datatable[0][0]
article = datatable[0][2]

def article_proc(article):
    art = article.split("▶")
    if len(art) > 1:
        icle = art[:-3]
        s = ""
        for t in icle:
            s += t
        article = s
    return article
article = article_proc(article)

comments = []
replys = []

for i in range(1,len(datatable)):
    line = datatable[i]
    if datatable[i-1][0] == datatable[i][0]:  #대댓글일때 (라인넘버, 대댓글본문)
        replys.append(line[:2])
    else:
        comments.append(line[:2]+line[4:])  #댓글일때 (라인넘버, 댓글본문, 답글갯수)

# In[]:

#okt
# def get_morphs(text):
#     tags = okt.pos(text, norm='True', stem='True')
#     l = [] 
#     for words in tags:  
#         l.append(words[0])
#     return l

# def get_nouns(text):
#     key = ["Noun"] 
#     tags = okt.pos(text, norm='True', stem='True')
#     l = [] 
#     for words in tags:  
#         if words[1] in key:
#             l.append(words[0])
#     return l
    
# def num_pos(text):
#     tags = okt.pos(text, norm='True', stem='True')
#     return len(tags)


# In[]:

#mecab
def get_morphs(text):
    tags = mecab.pos(text)
    l = [] 
    for words in tags:  
        l.append(words[0])
    return l

def get_nouns(text):
# 일반명사,고유명사
    key = ["NNG", "NNP"] 
    tags = mecab.pos(text)
    l = [] 
    for words in tags:  
        if words[1] in key:
            l.append(words[0])
    return l
    
def num_pos(text):
    tags = mecab.pos(text)
    return len(tags)


# In[]:

# 명사개수
def num_naive(text):
    nouns = get_nouns(text)
    return len(nouns)

# 명사종류개수
def num_only(text):
    nouns = get_nouns(text)
    return len(set(nouns))

# 본문포함된 명사개수
def num_naive_article(article, text):
    article_nouns = get_nouns(article)
    nouns = get_nouns(text)
    real_nouns = []
    for noun in nouns:
        if noun in article_nouns:
            real_nouns.append(noun)
    return len(real_nouns)

# 본문포함된 명사종류개수
def num_only_article(article, text):
    article_nouns = set(get_nouns(article))
    nouns = set(get_nouns(text))
    inter = nouns.intersection(article_nouns)
    return len(inter)

# processed comments and replys
proc_comments = []
# proc_replys = []

for comment in comments:
    content = comment[1]
    processing = comment + [num_pos(content), 
                            num_naive(content), 
                            num_only(content), 
                            num_naive_article(article, content), 
                            num_only_article(article, content)]
    proc_comments.append(processing)


# Jaccard Similarity
def jac_sim(article, text):
    article = set(get_morphs(article))
    comment = set(get_morphs(text))
    inter = comment.intersection(article)
    uni = comment.union(article)
    return len(inter)/len(uni)

def nonset_jac_sim(article, text):
    article = get_morphs(article)
    comments = get_morphs(text)
    inter = []
    for comment in comments:
        if comment in article:
            inter.append(comment)
    uni = set(comments).union(set(article))
    return len(inter)/len(uni)

def noun_jac_sim(article, text):
    article_nouns = set(get_nouns(article))
    nouns = set(get_nouns(text))
    inter = nouns.intersection(article_nouns)
    uni = nouns.union(article_nouns)
    return len(inter)/len(uni)

def nonset_noun_jac_sim(article, text):
    article_nouns = get_nouns(article)
    nouns = get_nouns(text)
    real_nouns = []
    for noun in nouns:
        if noun in article_nouns:
            real_nouns.append(noun)
    uni = set(nouns).union(set(article_nouns))
    return len(real_nouns)/len(uni)

    
# revised rated comments and replys    
rated_comments = []
# rated_replys = []

for comment in comments:
    content = comment[1]
#     n = num_pos(content)
    rating = comment + [num_pos(content),
                        num_naive_article(article, content) / (num_naive(content)+1), 
                        num_only_article(article, content) / (num_only(content)+1), 
                        jac_sim(article, content), 
                        nonset_jac_sim(article, content), 
                        noun_jac_sim(article, content), 
                        nonset_noun_jac_sim(article, content)]
    rated_comments.append(rating)


# part for sklearn, similarity

from sklearn.feature_extraction.text import TfidfVectorizer

def tfid_vectorize(article, comment):
 sent = (article, comment)
 tfidf_vectorizer = TfidfVectorizer()
 tfidf_matrix = tfidf_vectorizer.fit_transform(sent) #문장 벡터화 진행
 #idf = tfidf_vectorizer.idf_
 #print(dict(zip(tfidf_vectorizer.get_feature_names(), idf)))
 return tfidf_matrix

#Cosine_similarity

from sklearn.metrics.pairwise import cosine_similarity
def cos_sim(matrix):
 sim = cosine_similarity(matrix[0:1], matrix[1:2]) #첫번째와 두번째 문장 비교
 #array([[0.113]])
 return sim[0][0]

#Euclidean Distance or L2-Distance

from sklearn.metrics.pairwise import euclidean_distances
def euc_dis(matrix):
 sim = euclidean_distances(matrix[0:1], matrix[1:2])
 #array([[1.331]])
 return sim[0][0]

#L1-Normalization

def l1_normalize(v):
 norm = np.sum(v)
 return v / norm
def nor_euc_dis(matrix):
 tfidf_norm_l1 = l1_normalize(matrix)
 sim = euclidean_distances(tfidf_norm_l1[0:1], tfidf_norm_l1[1:2])
 # array([[0.212]])
 return sim[0][0]

#Manhattan Similarity or  L1-Distance

from sklearn.metrics.pairwise import manhattan_distances
def manh_dis(matrix):
 sim = manhattan_distances(matrix[0:1], matrix[1:2])
 #array([[0.857]])
 return sim[0][0]
def nor_manh_dis(matrix):
 tfidf_norm_l1 = l1_normalize(matrix)
 sim = manhattan_distances(tfidf_norm_l1[0:1], tfidf_norm_l1[1:2])
 #array([[0.857]])
 return sim[0][0]

# similarity commnets

similarity_comments = []

for comment in comments:
 content = comment[1]
 tfidf_matrix = tfid_vectorize(article, content)
 #tfidf_matrix = tfid_vectorize(summary, content)
 similarity = comment + [cos_sim(tfidf_matrix), euc_dis(tfidf_matrix), nor_euc_dis(tfidf_matrix), manh_dis(tfidf_matrix), nor_manh_dis(tfidf_matrix)]
 similarity_comments.append(similarity)


df0 = pd.DataFrame(comments, columns=['댓글번호','댓글본문','답글수'])
df1 = pd.DataFrame(proc_comments, columns = ['댓글번호','댓글내용','답글수','pos길이',
                                             '명사개수','명사종류개수',
                                             '본문명사개수','본문명사종류개수'])

new_df1 = df1.sort_values(by='본문명사개수', ascending=False)

df2 = pd.DataFrame(rated_comments, columns = ['댓글번호','댓글내용','답글수','pos길이',
                                              '본문/전체명사','본문/전체명사종류', 
                                              '자카드','nonset자카드',
                                              '자카드명사','nonset자카드명사'])

new_df2 = df2.sort_values(by='본문/전체명사', ascending=False)

df3 = pd.DataFrame(similarity_comments, columns = ['댓글번호','댓글내용','답글수',
                                                   '코사인유사도',
                                                   '유클리디언','norm유클',
                                                   '맨해튼','norm맨해'])

new_df3 = df3.sort_values(by='코사인유사도', ascending=False)

# In[]:


################
### for TEST ###  
################

like = dataset['기사본문/좋아요'].tolist()[1:]
dislike = dataset['none/싫어요'].tolist()[1:]

likes = [float(ke) for ke in like]
dislikes = [float(dke) for dke in dislike]

comment_only = df0['댓글본문'].tolist()
num = [n+1 for n in range(len(comment_only))]
replyN_only = df0['답글수'].tolist()

jaccard_only = df2['nonset자카드'].tolist()
cosine_only = df3['코사인유사도'].tolist()
euclidean_only = df3['norm유클'].tolist()

testList = df1['pos길이'].tolist()
testLog = cr.log_scale(testList, 2)
testNorm = cr.norm_data(testList)
testRank = cr.norm_rank(testList, True)

textRankN_only = ut.com_to_trscore(article, comment_only)




# In[]:

# reply list
n1_list = cr.norm_data(cr.log_scale(replyN_only, 2))


def list_calculate(l1, l2, k):
    if l2 == []:
        l = (np.array(l1)*k).tolist()

    else:
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

        elif k == -2:
            ldf = pd.DataFrame([l1]+[l2])
            ldf = ldf.T
            ldf[2] = (ldf[0] / ldf[1])**(1/2)
            l =ldf[2].tolist()

    return l

n2_list = cr.norm_data(cr.log_scale(list_calculate(likes,dislikes,1), 2))

n3_list = cr.norm_data(list_calculate(textRankN_only, jaccard_only, -2)) 

n4_list = list_calculate(cr.norm_rank(cosine_only, True), cr.norm_rank(euclidean_only, False), 2)

final = [num,comment_only,n1_list,n3_list,n3_list]

# print("a: {0}, b: {1}, c: {2}, d: {3}, e: {4}, f: {5}".format(len(num), len(comment_only), len(n1_list), len(n2_list), len(n3_list), len(n4_list)))

fdf = pd.DataFrame(final)

fdf.T

