import re
from application.remove_matches import remove_matches as rm

data = r'phonebook_raw.csv'
pattern = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
phone_patt = re.compile(pattern)
sub_pattern = r'+7(\3)\6-\8-\10 \12\13'

def fix_phonebook(cont_list):
    new_phonebook = list()
    for item in cont_list:
        full_name = ','.join(item[:3])
        result = re.findall(r'(\w+)', full_name)
        while len(result) < 3:
            result.append('')
        result.append(item[3])
        result.append(item[4])
        correct_phone = phone_patt.sub(sub_pattern, item[5])
        result.append(correct_phone)
        result.append(item[6])
        new_phonebook.append(result)
    return rm(new_phonebook)