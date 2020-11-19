from urllib.parse import quote
import urllib.request
from bs4 import BeautifulSoup as bs

def kor_dict_check(word):
  search_query = word
  search_query = quote(search_query, safe=':/?-=')
  auth_key = '3863F05BCC5098857F1DFD47AF07CFF0'
  url = 'https://stdict.korean.go.kr/api/search.do'+ '?q=' + search_query + "&key=" + auth_key
  request = urllib.request.Request(url)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()

  if rescode == 200:
    response_body = response.read()
  else:
    print("Error Code:" + rescode)
    return "Error Occured"

  xml = bs(response_body, 'lxml-xml')
  if xml.select('total')[0].get_text()=="0":
    return False
  else:
    return True

#print(kor_dict_check("베이니아"))