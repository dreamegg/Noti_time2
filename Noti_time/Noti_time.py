#-*- coding: utf-8 -*-  #한글을 쓸 때는 꼭 붙인다. 문자 인코딩을 UTF-8로 하겠다는 것이다. 인코딩은 앞으로 계속 속썩일 것이다.

import urllib #URL을 열고 HTML을 읽는 모듈, urllib을 불러온다
from bs4 import BeautifulSoup #bs4모듈에서 뷰티풀수프 함수를 불러옴

targetUrl = "https://underwood1.yonsei.ac.kr:8443/haksa/websquare/websquare.html?w2xPath=/haksa/wq/main.xml#"
soup = BeautifulSoup(urllib.urlopen(targetUrl).read()) #해당 웹주소 열고 뷰티풀수프로 긁어온 다음 soup라는 변수에 넣는다.
print soup.prettify()

raw_input("") 
