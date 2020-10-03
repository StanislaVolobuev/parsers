from selenium import webdriver


url = "https://www.e-katalog.ru/mtools/dot_output/mui_item_big_table.php?idg_=1666486"
url = "https://www.e-katalog.ru/mtools/dot_output/mui_item_big_table.php?idg_1666486"
driver = webdriver.Chrome()
driver.get(url)
# element = driver.find_elements_by_class_name("list-more-small")
# for elem in element:
    # print(elem.get_attribute('jsource'))
