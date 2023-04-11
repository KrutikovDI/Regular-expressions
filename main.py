from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# ## 1. Выполните пункты 1-3 задания.
# ## Ваш код
# создаем из contacts_list словарь
contacts_dict = []
for contact in contacts_list:
    contact_str = ' '.join(contact[0:3]).split(' ')[0:3] + contact[3:7]
    contact_dict = {'lastname' : contact_str[0],
            'firstname' : contact_str[1],
            'surname' : contact_str[2],
            'organization' : contact_str[3],
            'position' : contact_str[4],
            'phone' : contact_str[5],
            'email' : contact_str[6]
            }
    contacts_dict.append(contact_dict)
# находим дублирующие записи о человеке по фамилии/имени
# объединяем и обновляем значения, запись дубликат - удаляем
for j, p in enumerate(contacts_dict):
    for i, n in enumerate(contacts_dict):
        if n['lastname'] == p['lastname'] and n['firstname'] == p['firstname'] and i != j:
            contact1_list = list(contacts_dict[j].keys())
            contact2_list = list(contacts_dict[i].values())
            for n in range(7):
                if len(contact2_list[n]) != 0:
                    contacts_dict[j][contact1_list[n]] = contact2_list[n]
            del contacts_dict[i]
# создаем список записей без дублей
contacts_list_new = []
for n in range(len(contacts_dict)):
    contacts_list_new.append(list(contacts_dict[n].values()))
print(contacts_list_new)

# приводим все телефоны в формат +7(999)999-99-99 доб.9999
# построчно переводит список в строку, регулиркой форматируем номера и возвращаем в список 
contacts_list_new_telephone = []
for indx in range(len(contacts_list_new)):
    old_text = ' '.join(contacts_list_new[indx])
    pattern = r"(8|\+7)\s*\(*(\d{3})\)*-*\s*(\d{3})\-*(\d{2})\-*(\d{2})(\s*)\(*([доб.]*)\s*(\d*)\)*"
    sub_str = r"+7(\2)\3-\4-\5\6\7\8"
    new_text = re.sub(pattern, sub_str, old_text, re.M)
    contacts_list_new_telephone.append(new_text.split(' '))

# 2. Сохраните получившиеся данные в другой файл.
# ## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  
# ## Вместо contacts_list подставьте свой список:
  datawriter.writerows(contacts_list_new_telephone)