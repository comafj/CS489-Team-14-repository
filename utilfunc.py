from extraction import CS489_Keyword_Extraction_ver_0_2 as ke
import news as ns
import dict_check as dc
import get_comment as gc
import csv

# Function to make text rank based score
# Input : (indexing, num_k, num_rn)
#   indexing : tsv file indexing to indicate file sin old_data/crawling_output
#   num_k : number of keywords that will be used to search related news
#   num_rn : number of related news that will be used update keywords dictionary
# Output : final_result
#   final_result : List of tuple. Each tuple is composed of (index, score, comment)
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

# Another function to make textrank based score
# Input : (news_body, comments)
#   news_body : String type variable that indicates specific news article
#   comments : List of comments of specific news article
# Output : result
#   result : List of scores for each corresponding comment
def com_to_trscore(news_body, comments, num_k=3, num_rn=5):
    keywords = ke.keyfrombody(news_body) # Using news_body, initialize keyword score dictionary, keywords
    ids = keywords.keys() # Get keywords dictionary's keys

    top_keys = [] # Determine if there are any foreign words that can interfere with search
    for k in list(ids):
        if dc.kor_dict_check(k): # If the word is korean word,
            top_keys.append(k) # append them
        else:
            continue
        if len(top_keys)==num_k: # Until num_k has collected
            break

    related_news = ns.bscrawling(top_keys, num_rn) # With top important keys, find related news article

    for rn in related_news: # Using related news articles,
        new_key = ke.keyfrombody(rn)
        for candidate_word in new_key: # Update keyword dictionary keywords
            if candidate_word in keywords:
                keywords[candidate_word] += new_key[candidate_word]
            else:
                keywords[candidate_word] = new_key[candidate_word]

    com_scores = ke.bnew_ka(keywords, comments) # With updated keyword dictionary and comments list, get textrank score list
    result = com_scores
    return result
