import argparse, os, shutil

def read_folder(folder_path: str):
    img_list = os.listdir(folder_path)
    #count = 0
    for img in img_list:
        if img.endswith(".jpg"):
            #path = "python demo_img.py --images ./6/" + "defaultPrimary-0_streamType_u.jpg" + " --checkpoint-path ./pretrained_model/checkpoint_iter_370000.pth" 
            #path = "python demo_img.py --images ./6/" + img + " --checkpoint-path ./pretrained_model/checkpoint_iter_370000.pth"
            path = "python demo_img.py --images " + folder_path + "\\"+ img + " --checkpoint-path ./pretrained_model/checkpoint_iter_370000.pth"
            #count += 1
            #print(path)
            os.system(path)
    #print(count)

def dir_path(string) -> str:
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def main(folder_path: str):
    read_folder(folder_path)

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
    main(args.folder)
    check_tmp_folder(args.folder)