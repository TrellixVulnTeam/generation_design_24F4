#coding:utf-8
from actions.web_actions import *
from time import sleep
#���������
dd=create_browser('https://www.baidu.com')
sleep(5)
#�ر������
close_browser(dd)
