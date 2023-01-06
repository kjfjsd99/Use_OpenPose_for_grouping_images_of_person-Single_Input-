import os

def read_folder(path):
    img_list = os.listdir(path)
    for img in img_list:
        #path = "python demo_img.py --images ./6/" + "defaultPrimary-0_streamType_u.jpg" + " --checkpoint-path ./pretrained_model/checkpoint_iter_370000.pth" 
        path = "python demo_img.py --images ./6/" + img + " --checkpoint-path ./pretrained_model/checkpoint_iter_370000.pth"
        os.system(path)

def main(path):
    read_folder(path)

if __name__ == '__main__':
    path = "./6"
    main(path)