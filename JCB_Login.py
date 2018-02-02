# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:15:21 2018

@author: vincenthuang
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Firefox()
driver.get('https://ezweb.easycard.com.tw/Event01/JCBMainServlet')
driver.find_element_by_class_name('a1').click()

driver.find_element_by_id('accept').click()
driver.find_element_by_id('txtCreditCard1').clear()
driver.find_element_by_id('txtCreditCard1').send_keys('3567')
driver.find_element_by_id('txtCreditCard2').clear()
driver.find_element_by_id('txtCreditCard2').send_keys('33')
driver.find_element_by_id('txtCreditCard4').clear()
driver.find_element_by_id('txtCreditCard4').send_keys('4107')

driver.find_element_by_id('txtEasyCard1').clear()
driver.find_element_by_id('txtEasyCard1').send_keys('8200')
driver.find_element_by_id('txtEasyCard2').clear()
driver.find_element_by_id('txtEasyCard2').send_keys('8505')
driver.find_element_by_id('txtEasyCard3').clear()
driver.find_element_by_id('txtEasyCard3').send_keys('0001')
driver.find_element_by_id('txtEasyCard4').clear()
driver.find_element_by_id('txtEasyCard4').send_keys('7123')

driver.find_element_by_id('recaptcha-anchor').click()
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[5]').click()