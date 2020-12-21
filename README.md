# Social Ethics Assitant : Offering Tools with new Sorting Criteria :mag:
Group project (Team14) for 2020 Fall CS489 Computer Ethics and Social Issues

We want to act as an assistant by offering new and personalized sorting criteria in NAVER NEWS COMMENT.


### 🏠 [Homepage](https://github.com/comafj/CS489-Team-14-repository)


## :pushpin: Subject / Purpose
- Comments on a website can easily influence the initial opinions of people who are new to the article.
- However, in the current comment system, everyone sees the same comments ordered by the number of likes.
- If people can easily find their subjectivity without external influence, the number of victims of Internet public opinion will be reduced.
- In order for people to truly get their own thoughts, we don't just give one answer, 
  but we just give a tool and act as an assitant to help make their own answer.
<center> 
  *Help people to find their own opinion*
</center>

## Usage
### In Python
```python
import main as ma

# main() : main(URL, ST1, ST2, ST3, ST4, k)
# URL indicates news article of interest
# ST1 is your weight on number of replies
# ST2 is your weight on number of likes / dislikes
# ST3 is your weight on keyword based algorithm
# ST4 is your weight on similarity based algorithm
# k determines the detailed method of Like/dislike option
# in the part of like/dislike, the score calculated by (likes + k*dislikes)
title, article, result = ma.main(default_url, 1, 2, 3, 4, -1)

print(title)
print(article)
print(result)
```

## :blue_heart: File Configuration - MAIN 
### main.py
A file that defines the main function that performs all the procedures sequentially.
### crawling
In this folder, we implemented news data crawling part. It can bring some information like each comments, their like/dislike number, and so on.
### noun_proc.py
A file that defines all functions which are needed to calculate the score in main.py. (Konlpy, TextRank, Scikit-learn)
### utilfunc.py
A file that defines a function that allows to use the process of scoring comments using TextRank with other factors.

## :purple_heart: File Configuration - Sub 
### GUI_test.py
A simple implementation of the GUI. Results obtained from the GUI created with this file are implemented so that only the top three comments aligned with the set criteria are output.
### dict_check.py
It includes function to check whether the word is korean word or not.
A word like "펜실베이니아" is divided into "펜실" and "베이니아" which make the search result fail.
So checking process is needed.
### news.py
At extraction folder, some important keywords are extracted from the main news.
With these keywords, this file searches some relevant naver news articles.
### index.html, middle_page.py, result_page.py
A simple implementation of web using CGI. Configure the page using multiple styles defined in the css folder.

## :green_heart: File Configuration - Additional 
### crawling_output
In this folder, we save tsv format files that include results of crawling.
### extraction
In this folder, we implemented extracting part of meaningful keyword. "CS489_Keyword_Extraction_ver_0_1" file is using Textrank based method to do it.
### for_df_output.ipynb
A python file with jupyter notebook which is almost same with main.py, but we can easily compile the code and check the result with jupyter.
### text_processing
In this folder, we save all sorting outputs by all the indicators we have devised. (.tsv format, 6 articles)
noun_proc_n.ipynb describes those .tsv files. It includes all indicators and its algorithm.


# Author

👤 **Sol Han, Gisang Lee, Minseon Hwang, Sangwoo Jung**

* Github: [@pine-s](https://github.com/pine-s)
* Github: [@bobopack](https://github.com/bobopack)
* Github: [@comafj](https://github.com/comafj)
* Github: [@SangwooJung98](https://github.com/SangwooJung98)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/comafj/CS489-Team-14-repository/issues). 

## Show your support

Give a ⭐️ if this project helped you!

