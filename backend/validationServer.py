import re
reg_dict = {
    'name': "[a-zA-Z]",
    'email': "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
    'password': "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
}

usertype_list = ["Retailer", "Customer"]
def validateSignUP(post_data, field_list):
    for field in field_list:
        value =  post_data.get(field)
        if value:
            if field == 'usertype':
                if value not in usertype_list:
                    return False, 'Please provide valid {0} : {1}, should be in {2}' .format(field, value, usertype_list)   
            elif not (field in reg_dict and len(re.findall(reg_dict[field],value))):
                return False, 'Please provide valid {0} : {1}' .format(field, value)    
        else:
            return False, 'Please provide {0}' .format(field)
    return True, "Success"
     