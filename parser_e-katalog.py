from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#url = "https://www.e-katalog.ru/mtools/dot_output/mui_item_big_table.php?idg_=1666486"
url = "https://www.e-katalog.ru/GIGABYTE-X299X-AORUS-XTREME-WATERFORCE.htm"
driver = webdriver.Chrome()
driver.get(url)
element = driver.find_elements_by_name("num_prices_1666486").clik
print('element', element)
# for elem in element:
    # print(elem.get_attribute('jsource'))
