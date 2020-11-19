from extraction import CS489_Keyword_Extraction_ver_0_2 as ke
import news as ns
import dict_check as dc

if __name__ == '__main__':
    news_body = ke.newsfromtext("extraction/news_body.txt")
    keywords = ke.keyfrombody(news_body)
    ids = keywords.keys()
    top_keys = []
    num_k = 5
    for k in list(ids):
        if dc.kor_dict_check(k):
            top_keys.append(k)
        else:
            continue
        if len(top_keys)==num_k:
            break
    
    print("Top important keywords in main news are %s" %(" ".join(s for s in top_keys)))
    
    print("[1 / 3] Searching related news ...")
    num_rn = 5
    related_news = ns.bscrawling(top_keys, num_rn)
    print("[1 / 3] Search finished")
    
    print("[2 / 3] Updating keywords ...")
    for rn in related_news:
        new_key = ke.keyfrombody(rn)
        for candidate_word in new_key:
            if candidate_word in keywords:
                keywords[candidate_word] += new_key[candidate_word]
            else:
                keywords[candidate_word] = new_key[candidate_word]
    print("[2 / 3] Update finished")
    
    print("[3 / 3] Ranking comments ...")
    comment_scores = ke.keyword_analysis(keywords, "extraction/news_body.txt", "extraction/comment_test.txt")
    print("[3 / 3] Ended")    