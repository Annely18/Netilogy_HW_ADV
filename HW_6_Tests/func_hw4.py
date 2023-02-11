import requests

# ========== ЗАДАЧА 1 ==========
# Дан список с визитами по городам и странам. Напишите код, который возвращает
# отфильтрованный список geo_logs, содержащий только визиты из России."

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def visit_russia(list_):
    res = []
    for visit in list_:
        for city, country in visit.values():
            if country == 'Россия':
                res.append(visit)
    return res



# print(visit_russia(geo_logs))


# ========== ЗАДАЧА 2 ==========
# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unique_ids(dic):
    unique_ids_set = set()
    for value in dic.values():
        unique_ids_set.update(value)
    return list(unique_ids_set)

# print(unique_ids(ids))


# ========== ЗАДАЧА 4 ==========
# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def max_sale(list_):
    max_volume = 0
    company_ID = None
    for company, volume in stats.items():
        if volume > max_volume:
            max_volume = volume
            company_ID = company
    return f'Канал с максимальным объемом продаж: {company_ID}'

# print(max_sale(stats))


# ========== Yaapi ==========

def create_folder(file_path, token):
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {"path": file_path}
    response = requests.get(upload_url, headers=headers, params=params)
    if response.status_code == 404:
        response = requests.put(upload_url, headers=headers, params=params)
    return response

