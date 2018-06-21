import json
import sys

from validations import Validation


def parse(f):
    data = json.loads(f)
    description = data.get('fields').get('description')
    key_values = description.split('----\r\n')
    klen = len(key_values)
    description = {}
    for i in range(klen):
        key_values[i] = key_values[i].split('h4. ')[1]
        key_values[i] = key_values[i].split('h5. ')
        key_values[i] = [x.split('h6. ') for x in key_values[i]]
        key_l = len(key_values[i])
        if(key_l>1):
            desc_local = {}
            for j in range(1, key_l):
                l = len(key_values[i][j])
                if(l>1):
                    local_dict = {}
                    for k in range(1, l):
                        key_values[i][j][k] = key_values[i][j][k].split('\r\n')
                        n = len(key_values[i][j][k])
                        if n>=4:
                            value_list = [x.split('* ')[1].strip() for x in key_values[i][j][k][1: n-2]]
                            local_dict[key_values[i][j][k][0].strip()] = value_list
                        else: local_dict[key_values[i][j][k][0].strip()] = key_values[i][j][k][1].strip()
                    desc_local[key_values[i][j][0].split('\r\n')[0].strip()] = local_dict
                else:
                    key_values[i][j] = key_values[i][j][0].split('\r\n')
                    n = len(key_values[i][j])
                    if n>=4:
                        value_list = [x.split('* ')[1].strip() for x in key_values[i][j][1: n-2]]
                        desc_local[key_values[i][j][0].strip()] = value_list
                    else: desc_local[key_values[i][j][0].strip()] = key_values[i][j][1].strip()
            description[key_values[i][0][0].strip()] = desc_local
        else:
            key_values[i][0] = key_values[i][0][0].split('\r\n')
            n = len(key_values[i][0])
            if n>4:
                value_list = [x.split('* ')[1].strip() for x in key_values[i][0][1: n-2]]
                description[key_values[i][0][0].strip()] = value_list
            else: description[key_values[i][0][0].strip()] = key_values[i][0][1].strip()
    return description


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./parse.py <filepath>")
    else:
        f = open(sys.argv[1]).read()
        description = parse(f)
        Validation.validate(description)
