import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\ashis\git_python\prank")
    print(file_list)

    #(2)Foreach file rename file
    os.chdir(r"C:\Users\ashis\git_python\prank")
    #translation = {"0":None,"1":None, "2":None,"3":None,"4":None,"5":None,"6":None,"7":None,"8":None,"9":None}
    translation={"0123456789" : None }
    for file_name in file_list: os.rename(file_name, file_name.translate(translation))
                                   

rename_files ()

os.listdir(r"C:\Users\ashis\git_python\prank")

                           
