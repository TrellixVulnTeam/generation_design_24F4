#coding:utf-8
from actions.web_actions import *
from actions.excel_actions import *
from actions.email_action import *
from actions.code_actions import *
#���������
browser=create_browser('http://www.weather.com.cn/')

#���Ԫ��
click_element(browser,'//*[@id="txtZip"]')

#���������
set_input(browser,'//*[@id="txtZip"]','shanghai')

#���Ԫ��
click_element(browser,'//*[@id="txtZip"]')

#�ӳ�ִ��
sleep_time(1)

#���Ԫ��
click_element(browser,'//*[@id="show"]/ul/li')

#�ӳ�ִ��
sleep_time(1)

#�л�����ҳ��
switch_page(browser,2)

#���Ԫ��
click_element(browser,'//*[@id="someDayNav"]/li[2]/a')

#��ȡԪ��������
weather=get_element_txt(browser,'//*[@id="7d"]/ul/li[1]')

#��ӡ����
print_mem(weather)

#�����ʼ�
send_emails(['694625452@qq.com'],weather,'shanghai_weather')

#�ر������
close_browser(browser)
