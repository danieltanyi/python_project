"""Project 5
Problem Statement:
Often, we have a large number of files in a directory with names that do not follow a specific pattern or are not easy to understand. Renaming each file manually can be time-consuming and error-prone. To solve this problem, we need a program that can rename a large number of files in bulk, based on a specified pattern.

Question:
Can you develop a Python program that takes a directory path and a pattern as input, and renames all the files in the directory that match the pattern to a new name that follows the specified pattern?"""


import os

path = "C:/Users/dtarh/OneDrive/Desktop/Python-Project/images/"
#path =path.replace("\\","/")



print(path)

print(os.listdir(path)) #After writing/pasting your path DON'T FORGET to put '/' after the directory.

def main():
    i=1
    for filename in os.listdir(path):
        new_name = path + str(i) + '.jpg' #write the suitable file extension at the end as per your needs.
        old_name = path + filename
        os.rename(old_name,new_name)
        i+=1

main()