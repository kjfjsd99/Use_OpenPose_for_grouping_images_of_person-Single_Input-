import numpy as np
import settings
import cv2
import pathlib
import os, shutil

settings.init()

def check_one_bbox(count):
    if count > 1:
        settings.isTwoFrame = True

def setup(path_list: list) -> None:
    for path in path_list:
        abs_path = os.path.abspath(path)
        img_path = pathlib.PurePath(path)
        img = img_path.name
        parent_abs_path = abs_path.split(img)[0]
        if not os.path.exists(parent_abs_path + 'Front'):
            os.mkdir(parent_abs_path + 'Front')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Front_Left'):
            os.mkdir(parent_abs_path + 'Front_Left')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Front_Right'):
            os.mkdir(parent_abs_path + 'Front_Right')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Side_Left'):
            os.mkdir(parent_abs_path + 'Side_Left')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Side_Right'):
            os.mkdir(parent_abs_path + 'Side_Right')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Back'):
            os.mkdir(parent_abs_path + 'Back')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Back_Left'):
            os.mkdir(parent_abs_path + 'Back_Left')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Back_Right'):
            os.mkdir(parent_abs_path + 'Back_Right')
        else:
            print("file exists")
        if not os.path.exists(parent_abs_path + 'Others'):
            os.mkdir(parent_abs_path + 'Others')
        else:
            print("file exists")


def grouping_method(path_list: list, image_data: np.array) -> None:
    #print(path_list)
    print(image_data)
    for path in path_list:
        #print(type(path)s
        abs_path = os.path.abspath(path)
        img_path = pathlib.PurePath(path)
        img = img_path.name
        parent_folder = img_path.parent.name
        #print(parent_folder)
        parent_abs_path = abs_path.split(img)[0]
        print(abs_path)
        split_path = abs_path.split(parent_folder)[1]
        print(abs_path.split(parent_folder))
        print(split_path)
        #print(parent_abs_path)

        if settings.isTwoFrame == False:
            if (len(image_data)) == 18:
                if (np.all(image_data[:, 0] > 0)):
                    destination_path = parent_abs_path + "Front" + split_path
                    shutil.move(abs_path, destination_path) 
                    print("Front")
                if (image_data[0][0]) > 0 and (image_data[16][0]) < 0:
                    if (image_data[14][0]) < 0:
                        destination_path = parent_abs_path + "Side_Left" + split_path
                        shutil.move(abs_path, destination_path)  
                        print("Side_Left")
                    else:
                        destination_path = parent_abs_path + "Front_Left" + split_path
                        shutil.move(abs_path, destination_path)                     
                        print("Front_Left")

                if (image_data[0][0]) > 0 and (image_data[17][0]) < 0:
                    if (image_data[15][0]) < 0:
                        destination_path = parent_abs_path + "Side_Right" + split_path
                        shutil.move(abs_path, destination_path) 
                        print("Side_Right")
                    else:
                        destination_path = parent_abs_path + "Front_Right" + split_path
                        shutil.move(abs_path, destination_path)
                        print("Front_Right")
                if (image_data[0][0]) < 0 and (image_data[14][0]) < 0 and (image_data[15][0]) < 0:
                    print(image_data[2,:])
                    print(image_data[5,:])
                    if (image_data[5,:][1] - image_data[2,:][1])/(image_data[5,:][0] - image_data[2,:][0]) < 0: 
                        if abs(image_data[5,:][1] - image_data[2,:][1]) <= 5 or abs(image_data[5,:][0] - image_data[2,:][0]) <= 5:
                            destination_path = parent_abs_path + "Back" + split_path
                            shutil.move(abs_path, destination_path)
                            print("Back")
                        else:
                            destination_path = parent_abs_path + "Back_Left" + split_path
                            shutil.move(abs_path, destination_path)
                            print("Back_Left")
                    if (image_data[5,:][1] - image_data[2,:][1])/(image_data[5,:][0] - image_data[2,:][0]) > 0:
                        if abs(image_data[5,:][1] - image_data[2,:][1]) <= 5 or abs(image_data[5,:][0] - image_data[2,:][0]) <= 5:
                            destination_path = parent_abs_path + "Back" + split_path
                            shutil.move(abs_path, destination_path)
                            print("Back")
                        else:
                            destination_path = parent_abs_path + "Back_Right" + split_path
                            shutil.move(abs_path, destination_path)
                            print("Back_Right")
                #elif np.all(image_data[0, :]) > 0 and (image_data[16, :]) < 0:
                #    print("Front Left")
            else:
                print("The number of body points in human pose should be 18 (Openpose 18 keypoints)!")
        else:
            destination_path = parent_abs_path + "Others" + split_path
            #print(destination_path)
            shutil.move(abs_path, destination_path)  
            print("Can't over one bbox!")
 
    
   







