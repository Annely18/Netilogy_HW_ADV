import datetime
import os

# ========== 1 ==========
# Доработать декоратор logger в коде ниже. Должен получиться декортор,
# который записывает в файл 'main.log' дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась и возвращаемое значение. Функция test_1 в коде ниже также должна отработать без ошибок.

def logger(old_function):
  def new_function(*args, **kwargs):
    value = old_function(*args, **kwargs)
    data = f' дата и время: {datetime.datetime.now()}, название функции: {old_function.__name__}, аргументы: {args}, {kwargs}, значение: {value}\n'

    with open('main.log', 'a',  encoding='utf-8') as f:
        f.write(data)
    return value
  return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
      log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
      assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

# ========== 2 ==========
# Доработать парметризованный декоратор logger в коде ниже. Должен получиться декортор, который записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение. Путь к файлу должен передаваться в аргументах декоратора. Функция test_2 в коде ниже также должна отработать без ошибок.

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            value = old_function(*args, **kwargs)
            data = f' дата и время: {datetime.datetime.now()}, название функции: {old_function.__name__}, аргументы: {args}, {kwargs}, значение: {value}\n'
            with open(path, 'a', encoding='utf-8') as f:
                f.write(data)
            return value
        return new_function
    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()

# ========== 3 ==========
# Применить написанный логгер к приложению из любого предыдущего д/з.

import requests
from bs4 import BeautifulSoup
import lxml
from fake_headers import Headers
import json


@logger('hh_vacancy.log')
def hh():
    headers = Headers(browser="firefox", os="win").generate()
    HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
    html = requests.get(HOST, headers=headers).text
    soup = BeautifulSoup(html, features='lxml')
    all_vac_div = soup.find(id='a11y-main-content')
    vac_list = all_vac_div.find_all(class_='vacancy-serp-item__layout')
    result_list = []
    for vac in vac_list:
        vac_name_tag = vac.find('a', class_='serp-item__title')
        vac_link = vac_name_tag['href']
        vac_html = requests.get(vac_link, headers=headers).text
        vac_desc = BeautifulSoup(vac_html, features='lxml').find(class_='vacancy-description').text
        if 'Django' in vac_desc or 'Flask' in vac_desc:
            vac_name = vac_name_tag.text
            comp_name = vac.find('a', class_='bloko-link bloko-link_kind-tertiary').text.replace(u'\xa0', u' ')
            adress = vac.find(attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text.split(',')[0]
            salary_tag = vac.find('span', class_="bloko-header-section-3")
            if salary_tag is None:
                salary = ''
            else:
                salary = salary_tag.text.replace(u'\u202f', u' ')
            result_list.append({
                'name': vac_name,
                'link': vac_link,
                'salary': salary,
                'company': comp_name,
                'adress': adress
            })
    with open(r" vacancy_list.json", 'w', encoding='utf-8') as f:
        json.dump(result_list, f, ensure_ascii=False, indent=2)
    return result_list

# hh()



@logger('flat_generator.log')
def flat_generator(list_of_lists):
    sublist_index = 0
    while sublist_index < len(list_of_lists):
        sublist_index += 1
        item_index = 0
        sublist = list_of_lists[sublist_index - 1]
        while item_index < len(sublist):
            item = list_of_lists[sublist_index - 1][item_index]
            yield item
            item_index += 1

# list_ = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
# for i in flat_generator(list_):
#     print(i)