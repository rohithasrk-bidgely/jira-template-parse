import json
import sys

def parse(f):
    data = json.loads(f)
    description = data.get('fields').get('description')
    key_values = description.split('----\r\n')
    klen = len(key_values)
    result = {}
    for i in range(klen):
        key_values[i] = key_values[i].split('h5. ')[1]
        key_values[i] = key_values[i].split('h6. ')
        l = len(key_values[i])
        if(l>1):
            local_dict = {}
            for j in range(1, l):
                key_values[i][j] = key_values[i][j].split('\r\n')
                n = len(key_values[i][j])
                value_list = [x.split('* ')[1].strip() for x in key_values[i][j][1: n-2]]
                local_dict[key_values[i][j][0].strip()] = value_list
            result[key_values[i][0].split('\r\n')[0].strip()] = local_dict
        else:
            key_values[i] = key_values[i][0].split('\r\n')
            n = len(key_values[i])
            if n>4:
                value_list = [x.split('* ')[1].strip() for x in key_values[i][1: n-2]]
                result[key_values[i][0].strip()] = value_list
            else: result[key_values[i][0].strip()] = key_values[i][1].strip()
    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./parse.py <filepath>")
    else:
        f = open(sys.argv[1]).read()
        print(json.dumps(parse(f)))
