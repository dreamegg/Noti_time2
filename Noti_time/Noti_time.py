#-*- coding: utf-8 -*-  #�ѱ��� �� ���� �� ���δ�. ���� ���ڵ��� UTF-8�� �ϰڴٴ� ���̴�. ���ڵ��� ������ ��� �ӽ��� ���̴�.

import urllib #URL�� ���� HTML�� �д� ���, urllib�� �ҷ��´�
from bs4 import BeautifulSoup #bs4��⿡�� ��ƼǮ���� �Լ��� �ҷ���

targetUrl = "https://underwood1.yonsei.ac.kr:8443/haksa/websquare/websquare.html?w2xPath=/haksa/wq/main.xml#"
soup = BeautifulSoup(urllib.urlopen(targetUrl).read()) #�ش� ���ּ� ���� ��ƼǮ������ �ܾ�� ���� soup��� ������ �ִ´�.
print soup.prettify()

raw_input("") 
