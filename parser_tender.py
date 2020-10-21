import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver import ActionChains


url_first_list = 'https://www.rts-tender.ru/poisk/search?id=8516a53c-ad04-4f9c-8341-af9c83b7e7d9'

driver = webdriver.Chrome()


class tender:
    def __init__(self, deal):
        self.deal = deal
        self.details = []


    def add_details(self, details):
        self.details.append(details)


    def one_list(self):
        self.driver.get(url_first_list)
        print('loading page № 1')
        time.sleep(7)
        cards = driver.find_elements_by_xpath("//div[@class='cards']")
        for i in cards:
            print('element', i)
            soup_elem = bs(i.text, 'html.parser')
            print(soup_elem.prettify())


#### test ####
def one_page(url):
    driver.get(url)
    print('loading page № 1')
    time.sleep(7)
    cards = driver.find_elements_by_xpath("//div[@class='cards']")
    n = 1
    one_page_tend = []
    for i in cards:
        # print('element', i)
        soup_elem = bs(i.text, 'html.parser')
        card_deal = str(soup_elem).split('\n')
        # print(soup_elem.prettify())
        j = 0
        deal_list = []
        for k in card_deal:
            if len(k) < 25 and j < 6:
                j += 1
            else:
                deal_list.append(card_deal[j])
                j += 1
        print('deal \n\n', deal_list, '\n num', n)
        n += 1
        tend = tender(deal_list[1])
        tend.add_details(deal_list[10])
        tend.add_details(deal_list[3])
        tend.add_details(deal_list[19])
        tend.add_details(deal_list[0][9:-6])
        one_page_tend.append(tend)
        # print('tend\n', 'num', n, '\n', tend.deal, tend.details)
    button = driver.find_elements_by_xpath("//li[@class='active']/following-sibling::li")
    print("\n\n button\n\n", button)
    ### ActionChains(driver).move_to_element(button).click(button).perform()
    ### button.click()
    return one_page_tend

t = one_page(url_first_list)
for i in t:
    print(i.deal, i.details)


def get_next_page(url_first_list):

    page = one_page(url_first_list)

