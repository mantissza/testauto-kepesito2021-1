from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)

# * Variables
title = driver.find_element_by_id('title')
error = driver.find_element_by_xpath('/html/body/form/span')


#  Törli a mező tartalmát, majd tetszőleges karaktersorral kitölti.
def clear_and_fill_input(element, text):
    element.clear()
    element.send_keys(text)


# * TC01 : Helyes kitöltés esete:
#     * title: abcd1234
#     * Nincs validációs hibazüzenet
def test_tc01():
    clear_and_fill_input(title, 'abcd1234')
    assert error.text == ''


# * TC02 : Illegális karakterek esete:
#     * title: teszt233@
#     * Only a-z and 0-9 characters allewed.
def test_tc02():
    clear_and_fill_input(title, 'teszt233@')
    assert error.text == 'Only a-z and 0-9 characters allewed'


# * TC03 : Tul rövid bemenet esete:
#     * title: abcd
#     * Title should be at least 8 characters; you entered 4.
def test_tc03():
    clear_and_fill_input(title, 'abcd')
    assert error.text == 'Title should be at least 8 characters; you entered 4.'


# test_tc01()
# test_tc02()
# test_tc03()
