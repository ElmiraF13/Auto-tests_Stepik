from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_button(browser):
    browser.get(link)
#    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-wishlist")
    time.sleep(3)
    assert button, "No basket button on page"