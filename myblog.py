# -*- coding: utf-8 -*-

import urllib2
import re
html=urllib2.urlopen('http://terrynie.com/').read()
contents = re.findall('<h2 class="post-title"><a href="(.*?)">(.*?)</a>',html,re.S)#.group(1)
for content in contents:
    print "博客标题："+content[1]+"  http://terrynie.com"+content[0]
