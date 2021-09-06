from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)

# * Variables
a = driver.find_element_by_id('a')
b = driver.find_element_by_id('b')
c = driver.find_element_by_id('result')
submit_btn = driver.find_element_by_id('submit')


#  Törli a mező tartalmát, majd tetszőleges karaktersorral kitölti.
def clear_and_fill_input(element, text):
    element.clear()
    element.send_keys(text)


# * TC01 : Helyesen jelenik meg az applikáció betöltéskor
#     * a: <üres>
#     * b: <üres>
#     * c: <nem látszik>
def test_tc01():
    a_is_empty = a.get_attribute('value')
    b_is_empty = b.get_attribute('value')
    c_is_empty = c.text
    assert a_is_empty == '' and b_is_empty == '' and c_is_empty == ''


# * TC02 : Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10
def test_tc02():
    clear_and_fill_input(a, '2')
    clear_and_fill_input(b, '3')
    submit_btn.click()
    c_result = c.text
    assert c_result == '10'


# * TC03 : Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: NaN
def test_tc03():
    clear_and_fill_input(a, '')
    clear_and_fill_input(b, '')
    submit_btn.click()
    c_result = c.text
    assert c_result == 'NaN'


# test_tc01()
# test_tc02()
# test_tc03()
