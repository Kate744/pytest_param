import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_verify_button_presented_on_the_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	
	find_button = browser.find_element_by_class_name("btn-add-to-basket")
	button_name = find_button.get_attribute("type")
	time.sleep(5)


	assert "submit" == button_name

