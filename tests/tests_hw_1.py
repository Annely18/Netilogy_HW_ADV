from HW_6_Tests.func_hw4 import visit_russia, unique_ids, max_sale
import pytest

# 1
def test_visit_russia():
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
    res = visit_russia(geo_logs)

# 1.1
    def russia_in():
        for el in res:
            for v in el.values():
                assert 'Россия' in v

# 1.2
    @pytest.mark.parametrize(
        "foreign", ['Индия', 'Португалия', 'Франция']
    )
    def foreign_not_in(foreign):
        for el in res:
            for v in el.values():
                assert foreign not in v

# 1.3
    def is_list():
        assert isinstance(res, list)


# 2
def test_unique_ids():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    unique_ids_list = [213, 15, 54, 119, 98, 35]
    res = unique_ids(ids)
    assert isinstance(res, list)
    assert res.sort() == unique_ids_list.sort()


# 3
def test_max_sale():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    cor_answer = 'yandex'
    assert cor_answer in max_sale(stats)
    assert max_sale(stats) == f'Канал с максимальным объемом продаж: yandex'
