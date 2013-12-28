#! /usr/bin/python

import os
import filecmp # see http://docs.python.org/library/filecmp.html

MASACARE = True
DONT_KILL = False

# Compares a array of file paths with another array of file paths.
# This was needed to ake the program really flexible.
def compare_files(file_paths_1, file_paths_2, kill = DONT_KILL):
  for file_path_1 in file_paths_1:    
    for file_path_2 in file_paths_2:
      if (file_path_1 != file_path_2) and filecmp.cmp( str(file_path_1), str(file_path_2) ):
        print str(file_path_1)+" => "+str(file_path_2)
        file_paths_1.remove(file_path_2) # removes duplicate occurancess in output
        if kill:
          os.remove(file_path_2)
          file_paths_2.remove(file_path_2) # This is done so that file not found error does not occur in next itreration


# Gets the files in a directory and all its sub directories
# This was got from http://stackoverflow.com/questions/120656/directory-listing-in-python
def files_in_a_directory(directory_path):
  file_paths = []
  for dirname, dirnames, filenames in os.walk(directory_path):
    for filename in filenames:
      file_paths.append(os.path.join(dirname, filename))
  
  return file_paths



###############################################
#    The program really starts from here      #
###############################################

directory = raw_input("Enter directory path: ")
masacare = raw_input("Do you want to kill clones (Y/N): ")
kill = DONT_KILL
if masacare.strip() == "Y":
  kill = MASACARE
  print "All Clones will be killed HAHAHAHA :->"
else:
  print "Clones will be spared :-|"


file_paths_1 = files_in_a_directory(directory)
file_paths_2 = file_paths_1 + [] # copy contents of file_paths_1 to file_paths_2
compare_files(file_paths_1, file_paths_2, kill)
