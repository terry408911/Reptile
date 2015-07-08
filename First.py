# -*- coding: utf-8 -*-

import urllib2
import re
html_contents = urllib2.urlopen('http://v.dxsbb.com/ligong/463/').read()
links_info = re.findall('<li><a title=(.*?) rel=',html_contents,re.S)
for every_link in links_info:
    number = re.search('(\d+)',every_link,re.S).group(1)
    links = re.search("/(.*?)'",every_link,re.S).group(1)
    lesson_info = '第'+number +'集 地址：http://v.dxsbb.com/'+links
    print lesson_info
