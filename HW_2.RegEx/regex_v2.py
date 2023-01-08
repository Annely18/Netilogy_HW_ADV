import re
import csv

# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну.

# читаем адресную книгу в формате CSV в список contacts_list

file_name = "phonebook_raw.csv"

with open(file_name, encoding='utf-8') as file:
  rows = csv.reader(file, delimiter=",")
  contacts_list = list(rows)

# получить нормальный вид списка
def get_cor_contacts_list(cont_list):
    cor_list = []
    for line in cont_list:
        contact = ','.join(line)
        pattern_name = r"(^\w+)[,|\s]+(\w+)[,?|\s?](\,{3})?(\w*)[\,]+"
        contact_cor_name = re.sub(pattern_name, r"\1,\2,\3\4,", contact, flags=re.I)
        pattern_cor_tel = r"(\+7|7|8)?\s*(\(?(\d{3})?\)?|s*|-)[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]*(\d{2})(\s*)?\(?(доб.)?\s*(\d*)?\)?"
        contact_cor_tel = re.sub(pattern_cor_tel, r"+7(\3)\4-\5-\6\7\8\9", contact_cor_name).split(',')
        cor_list.append(contact_cor_tel)
    return cor_list

# объединить, убрать повторы
def merge_cont_list(cont_list):
    for cont_1 in cont_list:
        del cont_1[7:]
        for cont_2 in cont_list:
            if cont_1[0] == cont_2[0] and cont_1[1] == cont_2[1]:
                for n in range(7):
                    if cont_1[n] == '':
                        cont_1[n] = cont_2[n]
    new_contacts_list = []
    for contact in cont_list:
         if contact not in new_contacts_list:
            new_contacts_list.append(contact)
    return new_contacts_list

if __name__ == '__main__':
    cor_contacts_list = get_cor_contacts_list(contacts_list)
    new_cont_list = merge_cont_list(cor_contacts_list)

    with open("phonebook.csv", encoding='utf-8', mode="w", newline="") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_cont_list)
