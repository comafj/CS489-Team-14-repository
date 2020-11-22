import requests
from bs4 import BeautifulSoup
import random

from selenium import webdriver
import time
import math

### variable ###
# text
# sum_text
# head
# time
# comment
# comment_only
# cmt_time
# like
# dislike
# reply

# url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=055&aid=0000852893'
# url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=011&aid=0003822153'
url = 'https://news.naver.com/main/read.nhn?mode=LS2D&mid=sec&sid1=104&sid2=231&oid=003&aid=0010193524'

print("###################################################")
print("### Do not touch chrome webpage during crawling ###")
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
    except:
        break

# only-comment (for reply classification)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

contents = soup.select('span.u_cbox_contents')
comment_only = [content.text for content in contents]

btn_more = driver.find_element_by_css_selector('a.floating_btn_top')
btn_more.click()

# re-reply
btn_more = driver.find_elements_by_css_selector('a.u_cbox_btn_reply')
for elem in btn_more:
    try:
        elem.click()
    except:
        break

btn_more = driver.find_element_by_css_selector('a.floating_btn_top')
btn_more.click()

driver.execute_script("window.scrollTo(0, window.scrollY + 3000);")

# 더보기 계속 클릭하기
btn_more = driver.find_elements_by_css_selector('a.u_cbox_btn_more')
for elem in btn_more:
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        driver.execute_script("arguments[0].click();", elem)
        driver.execute_script("window.scrollTo(0, window.scrollY + 1000);")
        time.sleep(1)
    except:
        break

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# 기사제목 추출
article_head = soup.select('div.article_info > h3 > a')
head = article_head[0].text
# print("기사 제목 : " + article_head[0].text)

# 기사시간 추출
article_time = soup.select('div.sponsor > span.t11')
time = article_time[0].text

contents = soup.select('span.u_cbox_contents')
comment = [content.text for content in contents]

# contents = soup.select('span.u_cbox_date')
# cmt_time = [content.text for content in contents]

contents = soup.select('em.u_cbox_cnt_recomm')
like = [content.text for content in contents]

loglike = []
for i in range(len(like)):
    if int(like[i]) == 0:
        loglike.append(0)
    else:
        loglike.append(math.log(int(like[i]), 2))

contents = soup.select('em.u_cbox_cnt_unrecomm')
dislike = [content.text for content in contents]

logdislike = []
for i in range(len(dislike)):
    if int(dislike[i]) == 0:
        logdislike.append(0)
    else:
        logdislike.append(math.log(int(dislike[i]), 2))

contents = soup.select('span.u_cbox_reply_cnt')
reply = [content.text for content in contents]

# save result in .tsv file
f = open('crawling_output.tsv', 'w', -1, "utf-8")
f.write(head + '\t' + time + '\t' + text + '\t' + sum_text + '\n')
cnt = []
j = 0
for i in range(len(comment)):
    if j == len(comment_only):
        break
    if comment[i] == comment_only[j]:
        j += 1
        cnt.append(i)
cnt.append(len(comment))
j = 0
for i in range(len(comment)):
    if i == cnt[j]:
        j += 1
        f.write(str(j) + '\t' + comment[i] + '\t' + str(loglike[i]) + '\t' + str(logdislike[i]) + '\t' + reply[j - 1] + '\n') #  + '\t' + cmt_time[k]
    else:
        f.write(str(j) + '\t' + comment[i] + '\t' + str(loglike[i]) + '\t' + str(logdislike[i]) + '\n') #  + '\t' + cmt_time[k]
f.close()

driver.quit()
