import argparse, os, shutil

def dir_path(string) -> str:
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def check_tmp_folder(folder_path: str) -> None:
    tmp_folder_path = folder_path + "_tmp"   
    for folder in list(os.walk(tmp_folder_path)) :
        if not os.listdir(folder[0]):
            os.removedirs(folder[0])
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=dir_path, help='path to input image(s) folder')
    args = parser.parse_args()
    #path = "./6"
    check_tmp_folder(args.folder)