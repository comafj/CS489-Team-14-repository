#! C:\Users\Public\Anaconda3\python.exe
#-*- coding:utf-8 -*-
print("content-type:text/html; charset=utf-8\n\n")
import sys
import codecs
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#import os
#sys.path.insert(0, "C:/Users/Public/Anaconda3/Lib/site-packages")
#sys.path.insert(0, "C:\\Users\\Public\\Anaconda3\\Lib\\site-packages")
from pysource import news as ns
import cgi
import cgitb
import MySQLdb
import test2

cgitb.enable()
form = cgi.FieldStorage()
url = form.getvalue('url')
st1 = form.getvalue('standard1')
st2 = form.getvalue('standard2')
st3 = form.getvalue('standard3')
st4 = form.getvalue('standard4')
k = form.getvalue('ldoption')

#connection = MySQLdb.connect(user='root', password='qwe123', db='ethics', charset='utf8')
#cursor = connection.cursor()
#errorstr = "Not proper news url"

def main_page():
    html = """
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
        <title>Demo page 2</title>
      </head>
    <!--
    Sided Template
    https://templatemo.com/tm-527-sided
    -->
      <body>
        <form method='post'>
          <div class="columns-bg2">
            <!-- Logo & Intro -->
            <section id="logo" class="tm-section-logo">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-sm-6 offset-sm-3 col-md-6 offset-md-0">
                    <div class="tm-site-name-container">
                      <div class="tm-site-name-container-inner">
                        <h2 class="text-uppercase tm-text-primary tm-site-name">
                          MAIN PAGE
                        </h2>
                        <p class="tm-text-primary tm-site-description2">
                          Set your article : Naver news link
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-sm-6 offset-sm-3 col-md-12 offset-md-1 div-url">
                <input type='text' name='url' placeholder=' Enter URL' class="input-url">
              </div>
            </section>

            <section id="logo" class="tm-section-logo2">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-sm-6 offset-sm-3 col-md-6 offset-md-0">
                    <p class="tm-text-primary middle-index">
                      Set your standards
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-sm-6 offset-sm-3 col-md-12 offset-md-1 div-url">
                <div> Reply </div> <input type='range' name='standard1' class="input-stand" min="1" max="10" value="1" oninput="document.getElementById('value1').innerHTML=this.value;">
                <span id="value1" class="stand-result"></span>
              </div>
              <div class="col-sm-6 offset-sm-3 col-md-12 offset-md-1 div-url">
                <div> Like / Dislike </div> <input type='range' name='standard2' class="input-stand" min="1" max="10" value="1" oninput="document.getElementById('value2').innerHTML=this.value;">
                <span id="value2" class="stand-result"></span>
                <div> Additional option: </div>
                <div style="padding-left: 20px;">
                    <input type="radio" id="huey" name="ldoption" value="1" checked>
                    <label for="one"> LIKE + DISLIKE</label>
                </div>
                <div style="padding-left: 20px;">
                    <input type="radio" id="dewey" name="ldoption" value="0">
                    <label for="two"> ONLY LIKE </label>
                </div>
                <div style="padding-left: 20px;">
                    <input type="radio" id="louie" name="ldoption" value="-1">
                    <label for="three"> LIKE - DISLIKE </label>
                </div>
              </div>
              <div class="col-sm-6 offset-sm-3 col-md-12 offset-md-1 div-url">
                <div> Keyword </div> <input type='range' name='standard3' class="input-stand" min="1" max="10" value="1" oninput="document.getElementById('value3').innerHTML=this.value;">
                <span id="value3" class="stand-result"></span>
              </div>
              <div class="col-sm-6 offset-sm-3 col-md-12 offset-md-1 div-url">
                <div> Similarity </div> <input type='range' name='standard4' class="input-stand" min="1" max="10" value="1" oninput="document.getElementById('value4').innerHTML=this.value;">
                <span id="value4" class="stand-result"></span>
              </div>
            </section>

            <div style="text-align:center; padding-top:30px; padding-bottom:100px;">
              <input type='submit' value='ANALYSIS'/>
            </div>
          </div>
        </form>
        <!-- /.columns-bg -->
      </body>
    </html>
    """
    print(html)

try:
    test_u = url
    result = ns.get_news(test_u)
    test2.footer(url, st1, st2, st3, st4, k)
except:
    main_page()
