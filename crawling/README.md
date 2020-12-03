# Crawling News Data

##### Crawling data include news headline, news creation time, summary by AI bot, comments, creation time of comments, like & dislike of comments, and replies of comments.

### Requirements
- python=3.7.3
- requests
- BeautifulSoup (for accelerating to crawl data)
- selenium (for dynamic crawling)

##### Need to download appropriate version of chromedriver.exe
https://sites.google.com/a/chromium.org/chromedriver/downloads

### crawl.py
##### crawling(url): crawling url and return true if there is no removed-reply, and also return the contents of the news and about comments
##### log_scale(list, n): get list contains n-log of each elem in the list
##### norm_data(list): normalization of each elem in the list(largest one be 1, smallest one be 0)
##### norm_rank(list, rev): if rev is true, smallest one be 1, else largest one be 1

##
### crawling_output_idx.tsv format
##### 1st row: news_head news_creation_time news_contents
##### comment row: ith comment like dislike re-reply-num
##### re-reply: ith_of_owner_cmt comment like dislike
### Crawling output directory (Every execution makes different file dir)
#### ../crawling_output/crawling_output_idx.tsv

##
### Execution (in CS489-Team-14-repository dir)
##### python .\crawling\crawling.py

##
###### pine-s | dream4future@kaist.ac.kr | 20160688 | Sol Han
###### SangwooJung98 | dan0130@kaist.ac.kr | 20160579 | Sangwoo Jung
