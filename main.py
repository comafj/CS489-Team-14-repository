# -*- coding: utf-8 -*- 
import pandas as pd

from crawling import crawl as cr
import utilfunc as ut
import noun_proc as pr


#######################
### PLEASE TYPE URL ###  
#######################

default_url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=009&aid=0004704439'
# url = input("TYPE THE URL OF NAVER NEWS: ")

def main(URL, ST1, ST2, ST3, ST4, k):
    boo, title, article, comments, likes, dislikes, replys = cr.crawling(URL)
    if boo:
        dfIn = sub(title, article, comments, likes, dislikes, replys, k)
        dfIn[6] = ST1*dfIn[2] + ST2*dfIn[3] + ST3*dfIn[4] + ST4*dfIn[5]
        result_list = [comments, dfIn[6].tolist(), likes, dislikes, replys]
        result = pd.DataFrame(result_list)
        result = result.T
        result.columns = ['comment', 'score', 'like', 'dislike', 'reply']
        result = result.sort_values('score', ascending=False)
        final = result[['comment', 'like', 'dislike', 'reply']] #for webpage UI
        # final = result #for project report
        final = final.values.tolist()
        return title, article, final
    else:
        print("Oh this article cannot be processed")
        return

def sub(title, article, comments, likes, dislikes, replys, k):
    article = pr.article_proc(article)
    num = [n+1 for n in range(len(comments))]

    textRank = ut.com_to_trscore(article, comments)
    # values for similarity
    jaccard = []
    cosine = []
    euclidean = []
    for comment in comments:
        jaccard.append(pr.nonset_jac_sim(article,comment))
        tfidf_matrix = pr.tfid_vectorize(article,comment)
        cosine.append(pr.cos_sim(tfidf_matrix))
        euclidean.append(pr.nor_euc_dis(tfidf_matrix))

    val_list1 = cr.norm_data(cr.log_scale(replys, 2))
    val_list2 = cr.norm_data(cr.log_scale(pr.list_calculate(likes,dislikes,k), 2))
    val_list3 = cr.norm_data(pr.list_calculate(textRank, jaccard, 2)) 
    val_list4 = pr.list_calculate(cr.norm_rank(cosine, False), cr.norm_rank(euclidean, True), 2)

    # SHOULD we set this numbers
    a, b, c, d = 2.23, 3.35, 2.92, 4 # default : based on the pre-survey (+ d, max) 
    default = [num, comments, val_list1, val_list2, val_list3, val_list4]
    df = pd.DataFrame(default)
    df = df.T
    df = df.fillna(0)
    df[2] = a*df[2]
    df[3] = b*df[3]
    df[4] = c*df[4]
    df[5] = d*df[5]
    return df

# main() : main(URL, ST1, ST2, ST3, ST4, k)
title, article, result = main(default_url, 1, 1, 1, 1, -1)

