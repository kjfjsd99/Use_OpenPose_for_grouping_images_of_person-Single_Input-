import argparse, os

def read_folder(folder_path):
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

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def main(folder_path):
    read_folder(folder_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=dir_path, help='path to input image(s) folder')
    args = parser.parse_args()
    #path = "./6"
    main(args.folder)