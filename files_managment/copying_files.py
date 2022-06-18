#copyfile() = copies the content of a file
#copy() = does what copyfile() does + permission mode + destination can be a directory
#copy2() = does what copy() does + copies metadata (file's creation and modification items)

import shutil

shutil.copyfile(".\\files_managment\\test.txt",".\\files_managment\\copy.txt") #src,dst   source and destination
