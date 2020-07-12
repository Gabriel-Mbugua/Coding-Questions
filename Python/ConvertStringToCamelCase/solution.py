import re

def to_camel_case(text):
    lst = re.split('[- _]', text) 
    lst1 = [elem.capitalize() if indx !=0 else elem for indx,elem in enumerate(lst)]
    print(''.join(lst1))
    return ''.join(lst1)


to_camel_case("the_stealth_warrior")