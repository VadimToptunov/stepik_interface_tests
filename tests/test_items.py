import pytest
import time


class TestBookCatalogue():
	def test_add_to_basket_button_presents_on_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		browser.get(link)
		time.sleep(15)
		button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
		assert button.text != ""
