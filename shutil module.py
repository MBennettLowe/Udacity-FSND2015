import os

def rename_files():
    #get the files
    file_list = os.listdir(r"C:\Users\M\Desktop\Python")
    current_path = os.getcwd()
    print(file_list)
    os.chdir(r"C:\Users\M\Desktop\Python")

    #rename files to extract secret message
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    
rename_files()
