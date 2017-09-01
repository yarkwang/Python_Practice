'''
Created on 2017年6月20日

@author: wei.wang7
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common import desired_capabilities

driver=webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver=webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.OPERA)

driver=webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)

driver=webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities={'browserName':'htmlunit',
                          'version':'2',
                          'javascriptEnabled':True})