from importlib.resources import path
import time 
import os
import shutil


path = input("Enter the source folder name: ")
dest = input("Enter the destination folder name: ")

exist = os.path.exists(path)
walk = os.walk(path)
join = os.path.join()

ctime = os.stat(path).st_ctime


