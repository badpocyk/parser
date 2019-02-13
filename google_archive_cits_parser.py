from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import os

class Book:
    name = None
    pdf = False
    pdf_link = None
    gost = None
    mla = None
    apa = None

    def __init__(self, name):
        self.name = name
        self.pdf = False
        self.pdf_link = None
        self.gost = None
        self.mla = None
        self.apa = None

    def __str__(self):
        string = "Название: " + self.name + " наличие pdf: " + str(self.pdf) + " ссылка на pdf: " + str(self.pdf_link) + "\n ГОСТ: " + str(self.gost) + "\n MLA: " + str(self.mla) + "\n APA: " + str(self.apa)
        return string


def use_chrome_driver():
    dirname = os.path.dirname(__file__) + '\chromedriver.exe'
    driver = webdriver.Chrome(dirname)
    return driver


def use_firefox_driver():
    dirname = os.path.dirname(__file__) + '\geckodriver.exe'
    driver = webdriver.Chrome(dirname)
    return driver


def search(driver, search_request):
    driver.get("https://scholar.google.ru")
    search = driver.find_element_by_id("gs_hdr_tsi")
    hover = ActionChains(driver).move_to_element(search)
    hover.perform()
    search.send_keys(search_request)
    search_button = driver.find_element_by_id("gs_hdr_tsb")
    hover = ActionChains(driver).move_to_element(search_button)
    hover.perform()
    search_button.click()
    sleep(1)


def list_elements(driver, books_list):
    books_el = driver.find_elements_by_class_name("gs_or")
    for book_el in books_el:
        book = Book(book_el.find_element_by_tag_name("h3").text)
        try:
            book.pdf_link = book_el.find_element_by_css_selector(".gs_ggsd a ").get_attribute("href")
            book.pdf = True
        except:
            pass
        get_cits(driver, book_el, book)
        books_list.append(book)


def get_cits(driver, book_el, book):
    open_cit = book_el.find_element_by_css_selector(".gs_or_cit svg")
    hover = ActionChains(driver).move_to_element(open_cit)
    hover.perform()
    open_cit.click()
    sleep(1)
    table_rosw = driver.find_elements_by_css_selector("#gs_cit table tr")
    for row in table_rosw:
        if row.find_element_by_css_selector("th").text == 'ГОСТ':
            book.gost = row.find_element_by_css_selector("td").text
        elif row.find_element_by_css_selector("th").text == 'MLA':
            book.mla = row.find_element_by_css_selector("td").text
        elif row.find_element_by_css_selector("th").text == 'APA':
            book.apa = row.find_element_by_css_selector("td").text

    close_cit = driver.find_element_by_css_selector(".gs_vis .gs_md_hdr .gs_md_x .gs_ico")
    hover = ActionChains(driver).move_to_element(close_cit)
    hover.perform()
    close_cit.click()
    sleep(0.5)

def next_page(driver):
    try:
        next_link = driver.find_element_by_css_selector("#gs_res_ccl_bot  button.gs_btnPR")
        hover = ActionChains(driver).move_to_element(next_link)
        hover.perform()
        next_link.click()
    except:
        pass

    try:
        next_link = driver.find_element_by_css_selector("#gs_n  span.gs_ico_nav_next")
        hover = ActionChains(driver).move_to_element(next_link)
        hover.perform()
        next_link.click()
    except:
        pass

    sleep(2)


def get_list(search_request, browser_index, capcha, pages):
    books_list = []
    if browser_index == "Firefox":
        driver = use_firefox_driver()
    elif browser_index == "Google Chrome":
        driver = use_chrome_driver()
    search(driver, search_request)
    if capcha:
        sleep(80)
    for i in range(pages):
        list_elements(driver, books_list)
        next_page(driver)

    return books_list


if __name__ == '__main__':
    get_list("философия", "Google Chrome", True, 1)

