#File Management
#This is to automate the organization and manage the files on your computer,
import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            shutil.move(os.path.join(directory, filename), os.path.join(directory, 'TextFiles', filename))
        elif filename.endswith('.jpg'):
            shutil.move(os.path.join(directory, filename), os.path.join(directory, 'Images', filename))

#Enter your path directory here!
organize_files('/path/to/your/directory')
