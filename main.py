import os

def copying():
    init_path = input("Enter initial directory's path:\t")
    parent_dir = os.path.dirname(init_path)
    new_name = input("Enter result directory name:\t")
    final_path = os.path.join(parent_dir, new_name)

    while  os.path.exists(final_path):
        new_name = input("Such directory already exists! Enter another result directory name:\t")
        final_path = os.path.join(parent_dir, new_name)

    file_count = sum(len(files) for _, _, files in os.walk(init_path))
    qnt = 0

    if file_count == 0:
        print("There are no files in initial directory!")
        return

    os.mkdir(final_path)

    for curpath, dirnames, filenames in os.walk(init_path):
        print("Progress:", qnt/file_count*100, '%', sep='')
        cnt = 0
        for filename in filenames:
            qnt += 1
            cnt += 1
            name_beginning = os.path.split(curpath)[1] + '_' + str(cnt)
            name_ext = os.path.splitext(filename)[1]
            final_name = name_beginning + name_ext
            os.rename(curpath+'/'+filename, curpath+'/'+final_name)
            os.replace(curpath+'/'+final_name, final_path+'/'+final_name)
    
    print('Programm finished')

if __name__ == "__main__":
    copying()
