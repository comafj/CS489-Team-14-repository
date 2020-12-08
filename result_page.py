#! C:\Users\Public\Anaconda3\python.exe
#-*- coding:utf-8 -*-

import main as mp

import cgi
import cgitb
import MySQLdb
from urllib.parse import urlparse

# DEBUGGING
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# DEBUGGING

cgitb.enable()

def footer(url, st1, st2, st3, st4, k):
    a, b, c = mp.main(url, st1, st2, st3, st4, 1)
    news_title = "[종합] 코로나3차 대유행 공포…신규확진 569명 이틀째 500명대"
    news_body = "국내 신종 코로나바이러스 감염증(코로나19)의 '3차 대유행'이 본격적으로 진행되면서 27일 신규 확진자 수는 또다시 500명대를 나타냈다.  전날(583명)에 이어 이틀 연속 500명대를 기록한 것이다.  이틀 연속 500명 이상 확진자가 나온 것은 대구·경북 중심의 '1차 대유행'이 한창이던 3월 초 이후 약 9개월 만이다.  정부와 감염병 전문가들은 지금의 확산세를 꺾지 못하면 하루 1000명 이상 확진자가 나올 수도 있을 것으로 내다보고 있다.  중앙방역대책본부는 이날 0시 기준으로 코로나19 신규 확진자가 569명 늘어 누적 3만2887명이라고 밝혔다. 전날(583명)과 비교하면 14명 줄었다.  방역당국이 3차 유행을 공식화한 가운데 국내 코로나19 확진자는 빠른 속도로 늘고 있다.  이달 들어 일별 신규 확진자 수는 124명→97명→75명→118명→125명→145명→89명→143명→126명→100명→146명→143명→191명→205명→208명→222명→230명→313명→343명→363명→386명→330명→271명→349명→382명→583명→569명 등이다. 지난 8일부터 20일 연속 세 자릿수를 이어간 가운데 300명을 넘긴 날은 9차례고, 500명대는 2차례다.  신규 확진자 569명의 감염경로를 보면 지역발생이 525명, 해외유입이 44명이다.  신규 확진자가 나온 지역을 보면 서울 204명, 경기 112명, 인천 21명 등 337명이다. 수도권 지역발생 확진자는 전날(402명)보다 65명 줄었지만, 300명대를 기록하며 전체 지역발생의 64.2%를 차지했다.  비수도권의 경우 경남이 38명으로 가장 많고 이어 충남 31명, 전북·부산 각 24명, 충북 19명, 광주 13명, 전남 10명, 강원 8명, 울산 7명, 대전 5명, 세종·경북·제주 각 3명이다.  해외유입 확진자는 44명으로, 전날(30명)보다 14명 늘었다.  한편 사망자는 전날보다 1명 늘어 누적 516명이 됐다. 국내 평균 치명률은 1.57%다.  [김현정 기자 hjk@mkinternet.com]  ▶ 네이버 메인에서 '매일경제'를 받아보세요 ▶ 궁금한 제조과정 영상으로 보세요. '이렇게 만들죠' ▶ 아파트 살까 청약할까. 여기서 확인하세요. '매부리tv'  [ⓒ 매일경제 & mk.co.kr, 무단전재 및 재배포 금지]"

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />

        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,600" />
        <!-- Google web font "Open Sans" -->
        <link rel="stylesheet" href="css/all.min.css" />
        <link rel="stylesheet" href="css/bootstrap.min.css" />
        <link rel="stylesheet" href="css/templatemo-style.css" />
        <title>Demo page 3</title>
      </head>
    <!--
    Sided Template
    https://templatemo.com/tm-527-sided
    -->
      <body>
        <div class="columns-bg3">
          <!-- Logo & Intro -->
          <section id="logo" class="tm-section-logo">
            <div class="container-fluid">
              <div class="row">
                <div class="col-sm-6 offset-sm-3 col-md-6 offset-md-0">
                  <div class="tm-site-name-container">
                    <div class="tm-site-name-container-inner">
                      <h2 class="text-uppercase tm-text-third tm-site-name">
                        RESULT PAGE
                      </h2>
                      <p class="tm-text-third tm-site-description2">
                        The title and body of an article
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section class="tm-p-3-section-1">
            <div class="container-fluid">
              <div class="comment-out-contatiner">
                <div class="col-md-10 offset-md-1 comment-container">
                  <div class="title-text" style="width:100%;">
                    {news_title}
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section class="tm-p-3-section-1">
            <div class="container-fluid">
              <div class="comment-out-contatiner">
                <div class="col-md-10 offset-md-1 comment-container">
                  <div class="body-text" style="width:100%;">
                    {news_body}
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section id="logo" class="tm-section-logo">
            <div class="container-fluid">
              <div class="row">
                <div class="col-sm-6 offset-sm-3 col-md-6 offset-md-0">
                  <div class="tm-site-name-container">
                    <div class="tm-site-name-container-inner">
                      <p class="tm-text-third tm-site-description2">
                        The newly arranged comments are :
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!-- 1st Section, Full Width Image -->
          <section class="tm-p-3-section-1">
            <div class="container-fluid">
              <div class="comment-out-contatiner">
                <div class="col-md-10 offset-md-1 comment-container">
                  <div class="comment-text " style="width:60%;">
                    보수꼴통 집회 관련 확진자는 집요하게 통계내더만 어째 민노총 집회 확진자는 일언반구도 없나??
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      LIKE
                      <div style="padding:5px;">
                        <div class="info-number">
                          7
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      DISLIKE
                      <div style="padding:5px;">
                        <div class="info-number">
                          0
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      REPLY
                      <div style="padding:5px;">
                        <div class="info-number">
                          1
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="comment-out-contatiner">
                <div class="col-md-10 offset-md-1 comment-container">
                  <div class="comment-text " style="width:60%;">
                    대구때는 진짜 사람이 없을정도..번화가도 횡햇었는데..서울 경기 수도권 번화가 나가봐 ..젊은이들 아주바글바글..참네..진짜 개념없는 젊은애들투성이 드라
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      LIKE
                      <div style="padding:5px;">
                        <div class="info-number">
                          24
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      DISLIKE
                      <div style="padding:5px;">
                        <div class="info-number">
                          0
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      REPLY
                      <div style="padding:5px;">
                        <div class="info-number">
                          1
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="comment-out-contatiner">
                <div class="col-md-10 offset-md-1 comment-container">
                  <div class="comment-text " style="width:60%;">
                    급한대로 서울 경기 두 지역만 집중관리하면 안 됩니까? 인천도 확진자들 보면 다 서울 경기 확진자 접촉으로 나오던데...
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      LIKE
                      <div style="padding:5px;">
                        <div class="info-number">
                          2
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      DISLIKE
                      <div style="padding:5px;">
                        <div class="info-number">
                          0
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="comment-info" style="width:13%">
                    <div class="comment-info-inner">
                      REPLY
                      <div style="padding:5px;">
                        <div class="info-number">
                          0
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        <script src="js/jquery-3.3.1.min.js"></script>
      </body>
    </html>
    """
    print(html)
