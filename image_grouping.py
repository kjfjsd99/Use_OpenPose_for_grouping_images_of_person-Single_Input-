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
        abs_path = os.path.abspath(path) #E:\yaochun\Object_Tracking\Using-OpenPose-to-group-people-images--main\6\defaultPrimary-0_streamType_u3.jpg
        #print(abs_path)
        head, img_name = os.path.split(abs_path)
        #print(head) #E:\yaochun\Object_Tracking\Using-OpenPose-to-group-people-images--main\6
        #print(img_name) #defaultPrimary-0_streamType_u3.jpg
        grandparent_folder_abspath, folder = os.path.split(head)
        #print(grandparent_folder_abspath) #E:\yaochun\Object_Tracking\Using-OpenPose-to-group-people-images--main
        #print(folder) #6
        other_folder_path = grandparent_folder_abspath + "\\" + folder + "_tmp" + "\\"

        if not os.path.exists(other_folder_path + 'Front'):
            os.makedirs(other_folder_path + 'Front')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Front_Left'):
            os.makedirs(other_folder_path + 'Front_Left')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Front_Right'):
            os.makedirs(other_folder_path + 'Front_Right')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Side_Left'):
            os.makedirs(other_folder_path + 'Side_Left')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Side_Right'):
            os.makedirs(other_folder_path + 'Side_Right')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Back'):
            os.makedirs(other_folder_path + 'Back')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Back_Left'):
            os.makedirs(other_folder_path + 'Back_Left')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Back_Right'):
            os.makedirs(other_folder_path + 'Back_Right')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Others'):
            os.makedirs(other_folder_path + 'Others')
        else:
            print("file exists")
        

def grouping_method(path_list: list, image_data: np.array) -> None:
    #print(path_list)
    #print(image_data)
    for path in path_list:
        abs_path = os.path.abspath(path) #E:\yaochun\Object_Tracking\Using-OpenPose-to-group-people-images--main\6\defaultPrimary-0_streamType_u3.jpg
        #print(abs_path)
        head, img_name = os.path.split(abs_path)
        #print(head) #E:\yaochun\Object_Tracking\Using-OpenPose-to-group-people-images--main\6
        #print(img_name) #defaultPrimary-0_streamType_u3.jpg
        grandparent_folder_abspath, folder = os.path.split(head)
        #print(grandparent_folder_abspath) #E:\yaochun\Object_Tracking\Using-OpenPose-to-group-people-images--main
        #print(folder) #6
        other_folder_path = grandparent_folder_abspath + "\\" + folder + "_tmp" + "\\"

        if settings.isTwoFrame == False:
            if (len(image_data)) == 18:
                if (np.all(image_data[:, 0] > 0)):
                    destination_path = other_folder_path + "Front"
                    shutil.copy(abs_path, destination_path) 
                    print("Front")
                if (image_data[0][0]) > 0 and (image_data[16][0]) < 0:
                    if (image_data[14][0]) < 0:
                        destination_path = other_folder_path + "Side_Left"
                        shutil.copy(abs_path, destination_path)  
                        print("Side_Left")
                    else:
                        destination_path = other_folder_path + "Front_Left"
                        shutil.copy(abs_path, destination_path)                     
                        print("Front_Left")

                if (image_data[0][0]) > 0 and (image_data[17][0]) < 0:
                    if (image_data[15][0]) < 0:
                        destination_path = other_folder_path + "Side_Right"
                        shutil.copy(abs_path, destination_path) 
                        print("Side_Right")
                    else:
                        destination_path = other_folder_path + "Front_Right"
                        shutil.copy(abs_path, destination_path)
                        print("Front_Right")
                if (image_data[0][0]) < 0 and (image_data[14][0]) < 0 and (image_data[15][0]) < 0:
                    print(image_data[2,:])
                    print(image_data[5,:])
                    if (image_data[5,:][1] - image_data[2,:][1])/(image_data[5,:][0] - image_data[2,:][0]) < 0: 
                        if abs(image_data[5,:][1] - image_data[2,:][1]) <= 5 or abs(image_data[5,:][0] - image_data[2,:][0]) <= 5:
                            destination_path = other_folder_path + "Back"
                            shutil.copy(abs_path, destination_path)
                            print("Back")
                        else:
                            destination_path = other_folder_path + "Back_Left"
                            shutil.copy(abs_path, destination_path)
                            print("Back_Left")
                    if (image_data[5,:][1] - image_data[2,:][1])/(image_data[5,:][0] - image_data[2,:][0]) > 0:
                        if abs(image_data[5,:][1] - image_data[2,:][1]) <= 5 or abs(image_data[5,:][0] - image_data[2,:][0]) <= 5:
                            destination_path = other_folder_path + "Back"
                            shutil.copy(abs_path, destination_path)
                            print("Back")
                        else:
                            destination_path = other_folder_path + "Back_Right"
                            shutil.copy(abs_path, destination_path)
                            print("Back_Right")
                #elif np.all(image_data[0, :]) > 0 and (image_data[16, :]) < 0:
                #    print("Front Left")
            else:
                print("The number of body points in human pose should be 18 (Openpose 18 keypoints)!")
        else:
            destination_path = other_folder_path + "Others"
            #print(destination_path)
            shutil.copy(abs_path, destination_path)  
            print("Can't over one bbox!")
 
    
   







