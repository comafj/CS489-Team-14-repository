from extraction import CS489_Keyword_Extraction_ver_0_2 as ke
import news as ns

news_body = ke.newsfromtext("extraction/news_body.txt")
keywords = ke.keyfrombody(news_body)
ids = keywords.keys()
top_three = list(ids)[:3]

print("Top 3 important keywords in main news are %s" %(" ".join(s for s in top_three)))
#print(top_three) # 투표, 우편, 용지
print("Searching related news ...")
related_news = ns.bscrawling(top_three, 5)
print("Search finished\n")

print("Updating keywords ...")
for rn in related_news:
    new_key = ke.keyfrombody(rn)
    for candidate_word in new_key:
        if candidate_word in keywords:
            keywords[candidate_word] += new_key[candidate_word]
        else:
            keywords[candidate_word] = new_key[candidate_word]
print("Update finished\n")

print("Ranking comments ...")
comment_scores = ke.keyword_analysis(keywords, "extraction/news_body.txt", "extraction/comment_test.txt")
print("Ended\n")