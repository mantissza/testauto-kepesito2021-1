from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)

# * Variables
rand_color = driver.find_element_by_id('randomColor')
test_color = driver.find_element_by_id('testColor')
color_substring = 'background-color: rgb'
start_btn = driver.find_element_by_id('start')
stop_btn = driver.find_element_by_id('stop')
result = driver.find_element_by_id('result')


#  A játék el van indítva vagy sem?
def color_check():
    #  Megvizsgálom mi a klikkelést követő szín pontos css kódja.
    first_check = test_color.get_attribute('style')
    # Várunk, hogy változzanak a színek.
    time.sleep(2)
    second_check = test_color.get_attribute('style')
    #  True-val tér vissza, ha megegyezik a két szín, akkor leállt a JS függvény.
    return first_check == second_check


# * TC01 : Helyesen jelenik meg az applikáció betöltéskor:
#     * Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán.
#     * A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ]
def test_tc01():
    is_a_color = rand_color.get_attribute('style')
    test_color_is_empty = test_color.text
    assert color_substring in is_a_color and test_color_is_empty == '[     ]'


# * TC02 : El lehet indítani a játékot a start gommbal.
#     * Ha elindult a játék akkor a stop gombbal le lehet állítani.
def test_tc02():
    start_game = start_btn.click()
    #  Amikor megjelenik a color_substring-ben szereplő kifijezés a style attribútumban,
    #  az egy jele annak, hogy elindult a játék.
    assert color_substring in test_color.get_attribute('style')
    #  Ha eltér a két szín, akkor valóban leállt a JS függvény.
    assert not color_check()
    stop_game = stop_btn.click()
    #  Ha megegyezik a két szín, akkor valóban leállt a JS függvény.
    assert color_check()


# * TC03 : Eltaláltam, vagy nem találtam el.
#     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor
#     * a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a Correct! felirat jelenik meg.
#     * ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen.
def test_tc03():
    #  Gyors szimuláció
    start_game = start_btn.click()
    time.sleep(1)
    stop_game = stop_btn.click()
    #  Ellenőrzés
    if rand_color.get_attribute('style') == test_color.get_attribute('style'):
        assert result.text == 'Correct!'
    else:
        assert result.text == 'Incorrect!'


# test_tc01()
# test_tc02()
# test_tc03()
