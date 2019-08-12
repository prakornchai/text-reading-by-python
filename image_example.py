from PIL import Image
import pytesseract
import os
import getpass

def extract_text_from_image(image_file_name_arg):

    # IMPORTANT
    # if you have followed my instructions to install this dependence in above text explanatin
    # for my machine is
    # if you don't put the right path for tesseract.exe the script will not work
    username = getpass.getuser()
    # here above line get the username for your machine automatically
    tesseract_exe_path_installation="C:\\Users\\user\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd=tesseract_exe_path_installation

# specify the direction of your image files manually or use line bellow if the images are in the script directory in     folder  images
    # image_dir="D:\\GIT\\ai_example\\extract_text_from_image\\images"
    image_dir=os.getcwd()+"\\images"
    dir_seperator="\\"
    image_file_name=image_file_name_arg
    # if your image are in different format change the extension(ex. ".png")
    image_ext=".jpg"
    image_path_dir=image_dir+dir_seperator+image_file_name+image_ext

    print("=============================================================================")
    print("image used is in the following path dir:")
    print("\t"+image_path_dir)
    print("=============================================================================")

    img=Image.open(image_path_dir)
    text=pytesseract.image_to_string(img, lang="eng")
    #print(text)
    return text
# change the name "image_1" whith the name without extension for your image name
# image_file_name_arg="image_1"
image_file_name_arg="image"
# image_file_name_arg="image_3"
# image_file_name_arg="image_4"
# image_file_name_arg="image_5"
text=extract_text_from_image(image_file_name_arg)
print(text)
with open('do_re_mi.txt', 'w') as f:
    f.write(text)
import pyttsx3
import win32api, sys, os
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
