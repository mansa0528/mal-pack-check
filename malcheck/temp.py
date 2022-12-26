from os import walk

_res = {}



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


try:
    if __name__ == "__main__":
        main()
except Exception as ee:
    print("exception is : {}".format(ee))