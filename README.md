# CS489-Team-14-repository
Group project for 2020 Fall CS489 Computer Ethics and Social Issues

We want to provide social ethics assistants by offering tools with new sorting criteria.

## Subject / Purpose
- Comments on a website can easily influence the initial opinions of people who are new to the article.
- If people can easily find their subjectivity without external influence, the number of victims of Internet public opinion will be reduced.
<center> 
  *Help people to find their own opinion*
</center>

## File Configuration
### crawling
In this folder, we implemented news data crawling part. It can bring some information like each comments, their like/dislike number, and so on.
### extraction
In this folder, we implemented extracting part of meaningful keyword. "CS489_Keyword_Extraction_ver_0_1" file is using Textrank based method to do it.
### crawling_output
In this folder, we save tsv format files that include results of crawling.
### dict_check.py
It includes function to check whether the word is korean word or not.
A word like "펜실베이니아" is divided into "펜실" and "베이니아" which make the search result fail.
So checking process is needed.
### news.py
At extraction folder, some important keywords are extracted from the main news.
With these keywords, this file searches some relevant naver news articles.
### index.html, middle_page.py, result_page.py
A simple implementation of web using CGI. Configure the page using multiple styles defined in the css folder.
### GUI_test.py
A simple implementation of the GUI. Results obtained from the GUI created with this file are implemented so that only the top three comments aligned with the set criteria are output.
### utilfunc.py
A file that defines a function that allows to use the process of scoring comments using TextRank with other factors.
### main.py
A file that defines the main function that performs all the procedures sequentially.

## Usage
### In Python
```python
import main as ma

# main() : main(URL, ST1, ST2, ST3, ST4, k)
# URL indicates news article of interest
# ST1 is weight on number of replies
# ST2 is weight on number of likes / dislikes
# ST3 is weight on keyword based algorithm
# ST4 is weight on similarity based algorithm
# k determines the detailed method of Like/dislike option
title, article, result = ma.main(default_url, 1, 2, 3, 4, -1)

print(title)
print(article)
print(result)
```
