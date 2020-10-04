import requests as re
from bs4 import BeautifulSoup as bs

# url_prod = "https://www.e-katalog.ru/GIGABYTE-X299X-AORUS-XTREME-WATERFORCE.htm"
# url_prod ="https://www.e-katalog.ru/SAMSUNG-KVADRAT-COVER-FOR-GALAXY-NOTE20-ULTRA.htm"
# url_prod = "https://www.e-katalog.ru/PLANTRONICS-EXPLORER-ML15.htm"
url_prod = "https://www.e-katalog.ru/ATLANT-XM-4208-000.htm"

def product(url_prod):
    prod = re.get(url_prod)
    soup = bs(prod.text, 'html.parser')
    return soup


def get_url_spec():
    '''возвращает url страницы по кнопке "все характеристики"
    '''
    ''' проработать принимаемый аргумент'''
    soup = product(url_prod)
    div = soup.find('div', class_="list-more-small")
    elem = str(div).split()
    str_with_url = str(elem[6])
    list_url = str_with_url.split('=')
    urll = (list_url[1] + '=' + list_url[2]).split('"')
    url_spec = urll[1]
    return url_spec


def specifikations():
    '''  возвращает список характеристик и их значений
    '''
    ''' принимаемый аргумент
    '''
    url_spec = get_url_spec()
    spec = re.get(url_spec)
    soup_spec = bs(spec.content, 'html.parser')
    t = soup_spec.find_all(text=True)
    # /// # print(t)
    spec_list = []
    parameters = soup_spec.findAll('tr')
    for i in parameters:
        td = i.findAll('td')
        line = []
        for j in td:
            parameter = j.find_all(text=True)
            line.append(parameter)
            print('line', line)
            spec_list.append(list(line))
            '''проработать запись в эксель построчно или создание списка'''
    print(spec_list)


print(specifikations())


def name_product():
    '''принимаемый аргумент
    '''
    soup = product(url_prod)
    name = soup.find('h1', class_="t2 no-mobile")
    name_text = name.findAll(text=True)
    print(name_text)


print(name_product())


def get_market_url():
    '''
    проработать приннимаемый аргумент,
    во избежании двойного обращения к функции product
    '''
    soup = product(url_prod)
    url_markets = soup.findAll('table', class_="desc-hot-prices")
    price = soup.findAll('td', class_="model-shop-price")
    price_list = []
    for p in price:
        p1 = str(p).split('span')
        p2 = p1[-2]
        p2 = p2[1:-3]
        price_list.append(p2)
    all_price = []
    n_price = 0

    for shop in url_markets:
        name_shop = shop.find_all('u')
        for i in name_shop:
            name_and_url = []
            st = str(i)
            name = st[3:-4]
            a = i.parent
            url_shop = str(a).split('"')
            name_and_url.append(name)
            name_and_url.append(url_shop[9])
            all_price.append(name_and_url)
            n_price += 1

    for i in range(0, n_price):
        all_price[i].append(price_list[i])
    print('list', all_price)  # отфармотировать значение цены


# print(get_market_url())

