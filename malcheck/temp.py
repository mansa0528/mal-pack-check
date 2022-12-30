from os import walk
import re

_res = {'urls':[]}

def rEgx(files_to_open):
    _reg = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
    for _file in files_to_open:
        try:
            _f = open(_file,'r').read()
            x = re.findall(_reg,_f)
            _res['urls'] = _res.get('urls')+x
            break
        except Exception as e:
            print(e)
    return list(_res.values())


def get_files(_path):
    files_list,files = [],{}
    for i,j,k in walk(_path):
        if files.get(i) != None:
            files[i] = files[i]+k
        else:
            files[i] = k
    for _j in files:
        if len(files[_j]) != 0:
            for _i in files[_j]:
                files_list.append(_j+'/'+_i)
    return files_list


def main():
    directory_path = r'/home/ssambarathi/Documents/mal-pac/malcheck/test'
    list_of_files = (get_files(directory_path))
    print(rEgx(list_of_files))

try:
    if __name__ == "__main__":
        main()
except Exception as ee:
    print("exception is : {}".format(ee))