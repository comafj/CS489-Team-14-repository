import requests
from bs4 import BeautifulSoup
import random

from selenium import webdriver
import time

### variable ###
# text
# sum_text
# head
# time
# comment
# cmt_time
# like
# dislike
# reply

# url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=055&aid=0000852893'
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=011&aid=0003822153'

print("###################################################")
print("### DO not touch chrome webpage during crawling ###")
print("###################################################")

# 웹 드라이버
driver = webdriver.Chrome('./crawling/chromedriver.exe')
driver.implicitly_wait(30)
driver.get(url)

contents = driver.find_elements_by_css_selector('div._article_body_contents')
text = contents[0].text
text = text.replace('\n',' ')

btn_more = driver.find_element_by_css_selector('a.floating_btn_top')
btn_more.click()

btn_more = driver.find_element_by_css_selector('div.media_end_head_autosummary._auto_summary_wrapper')
btn_more.click()

summaries = driver.find_elements_by_css_selector('div._contents_body')
for summary in summaries:
    # print(summary.text)
    sum_text = summary.text
    sum_text = sum_text.replace('\n', ' ')

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

# 더보기 계속 클릭하기
while True:
    try:
        btn_more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        btn_more.click()
        # time.sleep(1)
    except:
        break

btn_more = driver.find_element_by_css_selector('a.floating_btn_top')
btn_more.click()

# re-reply
btn_more = driver.find_elements_by_css_selector('a.u_cbox_btn_reply')
for elem in btn_more:
    try:
        elem.click()
        # time.sleep(1)
    except:
        break

# 더보기 계속 클릭하기
while True:
    try:
        btn_more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        btn_more.click()
        # time.sleep(1)
    except:
        break

# 기사제목 추출
article_head = driver.find_elements_by_css_selector('div.article_info > h3 > a')
head = article_head[0].text
# print("기사 제목 : " + article_head[0].text)

# 기사시간 추출
article_time = driver.find_elements_by_css_selector('div.sponsor > span.t11')
time = article_time[0].text
# print("기사 등록 시간 : " + article_time[0].text)

contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
comment = []
for content in contents:
    # print(content.text)
    comment.append(content.text)

contents = driver.find_elements_by_css_selector('span.u_cbox_date')
cmt_time = []
for content in contents:
    # print(content.text)
    cmt_time.append(content.text)

contents = driver.find_elements_by_css_selector('em.u_cbox_cnt_recomm')
like = []
for content in contents:
    # print(content.text)
    like.append(content.text)

contents = driver.find_elements_by_css_selector('em.u_cbox_cnt_unrecomm')
dislike = []
for content in contents:
    # print(content.text)
    dislike.append(content.text)

contents = driver.find_elements_by_css_selector('span.u_cbox_reply_cnt')
reply = []
for content in contents:
    # print(content.text)
    reply.append(content.text)

# save result in .tsv file
f = open('crawling_output.tsv', 'w', -1, "utf-8")
f.write(head + '\t' + time + '\t' + text + '\t' + sum_text + '\n')
for i in range(len(reply)):
    f.write(str(i) + '\t' + comment[i] + '\t' + cmt_time[i] + '\t' + like[i] + '\t' + dislike[i] + '\t' + reply[i] + '\n')
    for j in range(int(reply[i])):
        f.write(str(i) + '\t' + comment[j] + '\t' + cmt_time[j] + '\t' + like[j] + '\t' + dislike[j] + '\n')
f.close()
