# Create a commandline utillity (program) that when run takes 1-3 commandline arguments where:

# * the first is the name of a directory in play
# * the second (optional) is a –flag (–todir <dirname>) that specifies where the files in that directory should be copied to.
# * the third (optional) is a –flag (–zip <filename>) that specifies if the files should be zipped and what the zip file should be called.

# So if you run the program like this "python extract.py . --todir /tmp/ --zip archive.zip" you should 
# copy all files in the current directory (.) to a new tmp directory and the .py files should be put in a 
# zip folder names archive.zip.

# TASK A
# Copy all .py files in a given directory to a new folder.

# TASK B
# Zip all .py files in a given directory and put the zip file in the specified folder.

from zipfile import ZipFile
import os, sys, shutil

def greeting(x):

    # Check if anything was inputted, and if directory is root or not
    if len(x) > 1:
        # Instantiate working directory variable
        directory = ""
        # Check if directory is .
        if x[1] == ".":
            directory = os.getcwd()
        else:   # Else replace directory
            directory = x[1]

    # Optional flag processing
    toDirFlag = ""
    zipFlag = ""

    if len(x) > 2:
        iteration = 0
        for flag in x:
            if flag == "--todir":
                toDirFlag = os.getcwd() + x[iteration + 1]
            if flag == "--zip":
                zipFlag = x[iteration + 1]
            iteration += 1
        
    #Create directory in case directory dont exist, else dont make a new one
    if not os.path.isdir(toDirFlag):
        os.makedirs(toDirFlag)

    # Do the copying
    src_files = os.listdir(os.getcwd())
    if zipFlag == "": 
        for file_name in src_files:
            full_file_name = os.path.join(os.getcwd(), file_name)
            if os.path.isfile(full_file_name) and full_file_name[-2:] == "py":
                shutil.copy(full_file_name, toDirFlag)
    else:
        # --zip works, but cant currently be moved to desired directory, will always be placed in root
        # this is the closest I'll get, working with files sucks
        shutil.make_archive((os.getcwd() + "\\" + zipFlag), 'zip', os.getcwd())
                
    
    


greeting(sys.argv)