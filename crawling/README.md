# Crawling News Data

##### Crawling data include news headline, news creation time, summary by AI bot, comments, creation time of comments, like & dislike of comments, and replies of comments.

### Requirements
- python=3.7.3
- requests
- BeautifulSoup (for accelerating to crawl data)
- selenium (for dynamic crawling)

##### Need to download appropriate version of chromedriver.exe
https://sites.google.com/a/chromium.org/chromedriver/downloads

### crawling_output.tsv format
##### 1st row: news_head news_creation_time news_contents news_summary
##### comment row: ith comment cmt_creation_time like dislike re-reply
##### re-reply: ith_of_owner_cmt comment cmt_creation_time like dislike

### Execution (in CS489-Team-14-repository dir)
##### python .\crawling\crawling.py

##
###### pine-s | dream4future@kaist.ac.kr | 20160688 | Sol Han
###### SangwooJung98 | dan0130@kaist.ac.kr | 20160579 | Sangwoo Jung
