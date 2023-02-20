import os
import shutil
from_dir = "C:/Users/Manasvi Bakshi/Downloads/exemplar_circles.pdf"
to_dir = "C:/Users/Manasvi Bakshi/Desktop/p111/ch10.pdf"
#list_of_files = os.listdir(from_dir)
root,extension = os.path.splitext(from_dir)
#print(list_of_files)
print("The root elements are", root)
print("The extension element is", extension)
dest = shutil.copy(from_dir, to_dir)
print("The file has been copied!")