def remove_matches(original_list):
    for contact in original_list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in original_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]            
    result_list = list()
    for i in original_list:
        if i not in result_list:
            result_list.append(i)
    return result_list