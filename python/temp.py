#coding:utf-8
from actions.web_actions import *
from actions.excel_actions import *
#���������
driver=create_browser('https://www.baidu.com')

#�л�����ҳ��
switch_page(driver,2)

#ˢ��ҳ��
refresh_page(driver)

#��ȡ����Ԫ��
elements=get_all_element(driver,'//*/)

#�ر������
close_browser(driver)

#��Excel�ļ�
book=open_excel('D://test1,xlsx')

#д������
insert_into_excel(book,'A1','hhh')
