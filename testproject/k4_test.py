from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.headless = False

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)

# * Variables
ascii_table = driver.find_element_by_xpath('/html/body/div/div/p[3]')
chr_i = driver.find_element_by_id('chr')
op_i = driver.find_element_by_id('op')
num_i = driver.find_element_by_id('num')
submit_btn = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')


# * TC01 : Helyesen betöltődik az applikáció:
#     * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#       * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~
def test_tc01():
    excepted_ascii_table ="!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    assert ascii_table.text == excepted_ascii_table


# * TC02 : Megjelenik egy érvényes művelet:
#     * chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#     * op mező vagy + vagy - karaktert tartlamaz
#     * num mező egy egész számot tartalamaz
def test_tc02():
    #  Szerepel az ascii táblában a chr?
    assert chr_i.text in ascii_table.text
    #  Az op - vagy + jelet jelez ki?
    assert op_i.text in '+-'
    #  A num egy egész számot jelöl?
    assert num_i.text.isnumeric()


# * TC03 : Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#     * A megjelenő chr mezőben lévő karaktert kikeresve a táblában
#     * Ha a + művelet jelenik meg akkor balra lépve ha a - akkor jobbra lépve
#     * A num mezőben megjelenő mennyiségű karaktert
#     * az result mező helyes karaktert fog mutatni
def test_tc03():
    #  Visszaadja hanyadik helyen szerepel.
    i_start = int(ascii_table.text.index(chr_i.text))
    #  Várt index kiszámítása
    if op_i.text == '+':
        i_excepted_result = i_start + int(num_i.text)
    else:
        i_excepted_result = i_start - int(num_i.text)
    #  Lekérjük az eredményt, majd összehasonlítjuk.
    submit_btn.click()
    assert ascii_table.text[i_excepted_result] == result.text


# test_tc01()
# test_tc02()
# test_tc03()
