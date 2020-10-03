import requests as re
from bs4 import BeautifulSoup as bs
url_prod = "https://www.e-katalog.ru/GIGABYTE-X299X-AORUS-XTREME-WATERFORCE.htm"
# url1 = "https://www.e-katalog.ru/ATLANT-XM-4208-000.htm"

def product(url_prod):
    prod = re.get(url_prod)
    soup = bs(prod.text, 'html.parser')
    div = soup.find('div', class_="list-more-small")
    # print(div)
    elem = str(div).split()
    str_with_url = str(elem[6])
    # print(str_with_url, type(str_with_url))
    list_url = str_with_url.split('=')
    urll = (list_url[1] + '=' + list_url[2]).split('"')
    url_spec = urll[1]
    return url_spec


def specifikations():
    url_spec = product(url_prod)
    spec = re.get(url_spec)
    soup_spec = bs(spec.content, 'html.parser')
    # colomn = soup_spec.find_all('td', class_="\"op01\"")
    t = soup_spec.find_all(text=True)
    print(t)
    spec_list=[]
    test = soup_spec.findAll('tr')
    for i in test:
        td = i.findAll('td')
        sp=[]
        for j in td:
            test = j.find_all(text=True)
            sp.append(test)
        print('sp', sp)





    # for tag in t:

        # print(tag)

    '''
    for item in items:
        for tag in item.find_all('span'):
            recipe_title = tag.text.strip()
            titles.append(recipe_title)
'''


    # colomn_1 = soup_spec.find_all('table', cellpadding='"\"3\""')
    # for elem in soup_spec:

    #    print(elem.get_text())

    # print(soup_spec.get_text())
    # print(colomn)
print(specifikations())

'''
#print(t, type(t))


ppp = re.get(t)
soup1 = bs(ppp.text, 'html.parser')
print(soup1)

'''
'''
https://www.e-katalog.ru/mtools/dot_output/mui_item_big_table.php?idg_=384697
def go_to_spec():
    url=open_spec(url1)
    list_spec=re.get(url)
    print(list_spec.text)

print(go_to_spec())


#for link in soup.find_all('a'):
#    print(link.get('href'))

'''



