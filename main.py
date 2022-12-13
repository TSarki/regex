import re
from pprint import pprint
import csv
from application.fixphonebook import fix_phonebook as fp, data as data


if __name__ == '__main__':
    with open(data, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)    
    
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(fp(contacts_list))
    



