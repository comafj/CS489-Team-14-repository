import os
import math
import time
import random

import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

default_url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=009&aid=0004704439'

def crawling(url):
    # print("###################################################")
    # print("### Do not touch chrome webpage during crawling ###")
    # print("###################################################")

    # 웹 드라이버
    driver = webdriver.Chrome(ChromeDriverManager().install())
<<<<<<< HEAD
=======
    # driver = webdriver.Chrome('./crawling/chromedriver')
>>>>>>> 4c2088f811de37582f9392e2a3b6dcf91a4611ca
    driver.implicitly_wait(30)
    driver.get(url)

    # news contents
    contents = driver.find_elements_by_css_selector('div._article_body_contents')
    content = contents[0].text
    content = content.replace('\n',' ')

    btn_more = driver.find_element_by_css_selector('span.u_cbox_in_view_comment')
    btn_more.click()

    cleanbot = driver.find_element_by_css_selector('a.u_cbox_cleanbot_setbutton')
    cleanbot.click()
    time.sleep(1)
    cleanbot_disable = driver.find_element_by_xpath("//input[@id='cleanbot_dialog_checkbox_cbox_module']")
    cleanbot_disable.click()
    time.sleep(1)
    cleanbot_confirm = driver.find_element_by_css_selector('button.u_cbox_layer_cleanbot2_extrabtn')
    cleanbot_confirm.click()
    time.sleep(1)

    # click more btn
    while True:
        try:
            btn_more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
            btn_more.click()
        except:
            break

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    # news head
    article_head = soup.select('div.article_info > h3 > a')
    head = article_head[0].text
    # comments
    contents = soup.select('span.u_cbox_contents')
    comment = [content.text for content in contents]
    # likes
    contents = soup.select('em.u_cbox_cnt_recomm')
    like = [int(content.text) for content in contents]
    # dislike
    contents = soup.select('em.u_cbox_cnt_unrecomm')
    dislike = [int(content.text) for content in contents]
    # reply cnt
    contents = soup.select('span.u_cbox_reply_cnt')
    reply = [int(content.text) for content in contents]

    driver.quit()
    boo = len(comment) == len(like) == len(dislike) == len(reply)
    return boo, head, content, comment, like, dislike, reply # if !boo, some of news comments have been removed

def log_scale(input, n): # logn(x+1): 0(if x == 0)
    l = []
    for elem in input:
        if elem >= 0:
<<<<<<< HEAD
            l.append(math.log(elem + 1, n))
        else:
            l.append(-math.log(-elem + 1, n))
    return l
=======
            l.append(math.log((elem) + 1, n))
        else:
            l.append(-math.log((-elem) + 1, n))
    return l

>>>>>>> 4c2088f811de37582f9392e2a3b6dcf91a4611ca

def norm_data(input): # range: 0(smallest) ~ 1(largest)
    return [(elem-min(input))/(max(input)-min(input)) for elem in input]

def norm_rank(input, rev): # If rev, smallest = 1. Else, largest = 1.
    temp = sorted([(elem, i) for i, elem in enumerate(input)], reverse = rev)
    temp = sorted([(idx, i) for i, (elem, idx) in enumerate(temp)])
    return norm_data([i for (idx, i) in temp])

#crawling(default_url)
