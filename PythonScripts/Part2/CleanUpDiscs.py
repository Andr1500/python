import os
import time

DAYS = 5   #max age of the file to stay
FOLDERS = [
           "/home/a1500/gitrepo/python/PythonScripts/Part2/others/"
          ]

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILES = 0
TOTAL_DELETED_DIRS = 0

now_time = time.time()  #gets current time in Secods
age_time = now_time - 60*60*24*DAYS


def delete_old_files(folder):
    """delete the files older than X days"""
    global TOTAL_DELETED_FILES
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)   #gets full Path to file
            file_time = os. path.getmtime(file_name)
            if file_time < age_time:
                size_file = os.path.getsize(file_name)
                TOTAL_DELETED_SIZE += size_file  #count sum of all free space
                TOTAL_DELETED_FILES += 1  #count of deleted foles
                print("deleting file: " + str(file_name))
                os.remove(file_name)


def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_now = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_now += 1
            print("deleting empty dir. " + str(path))
            os.rmdir(path)
    if empty_folders_now > 0:
        delete_empty_dir(folder)

# ------- main loop ----

start_time = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_empty_dir(folder)

finish_time = time.asctime()

print("------------")
print("start time: " + str(start_time))
print("total deleted size: " + str(int(TOTAL_DELETED_SIZE/1024)) + "kB")
print("total deleted files: " + str(TOTAL_DELETED_FILES))
print("total deleted empty folders: " + str(TOTAL_DELETED_DIRS))
print("finish time: " + str(finish_time))