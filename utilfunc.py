from extraction import CS489_Keyword_Extraction_ver_0_2 as ke
import news as ns
import dict_check as dc
import get_comment as gc
import csv

def make_tr_score(indexing, num_k=3, num_rn=5):
    file_i = str(indexing)
    file_form = "./crawling_output/old_data/crawling_output_" + file_i + ".tsv"
    news_body = gc.tsv_body(file_form)
    keywords = ke.keyfrombody(news_body)
    ids = keywords.keys()

    top_keys = []
    for k in list(ids):
        if dc.kor_dict_check(k):
            top_keys.append(k)
        else:
            continue
        if len(top_keys)==num_k:
            break

    related_news = ns.bscrawling(top_keys, num_rn)

    for rn in related_news:
        new_key = ke.keyfrombody(rn)
        for candidate_word in new_key:
            if candidate_word in keywords:
                keywords[candidate_word] += new_key[candidate_word]
            else:
                keywords[candidate_word] = new_key[candidate_word]

    final_result = []
    com_scores = ke.new_ka(keywords, gc.only_tsv_comments(file_form))
    com_scores = sorted(com_scores, key=lambda x: x[1], reverse=True)
    final_result = com_scores
    return final_result
