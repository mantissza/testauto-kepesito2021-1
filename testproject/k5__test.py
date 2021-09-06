from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)

# * Variables
bingo_nums = driver.find_elements_by_name('number')
checkbox_nums = driver.find_elements_by_xpath('//*[@id="numbers-list"]//input[@type="checkbox"]')


#  Törli a mező tartalmát, majd tetszőleges karaktersorral kitölti.
def clear_and_fill_input(element, text):
    element.clear()
    element.send_keys(text)


# * TC01 : Az applikáció helyesen megjelenik:
#     * A bingo tábla 25 darab cellát tartalmaz
#     * A számlista 75 számot tartalmaz
def test_tc01():
    assert len(bingo_nums) == 25
    assert len(checkbox_nums) == 75


# * TC02 : Bingo számok ellenőzrzése:
#     * Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
#     * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről
#       tényleg a már kihúzott számok közül kerültek-e ki
def test_tc02():
    assert True


# * TC03 : Új játékot tudunk indítani
#     * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
#     * új bingo szelvényt kapunk más számokkal.
def test_tc03():
    assert True


# test_tc01()
# test_tc02()
# test_tc03()
