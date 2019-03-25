import sys
import os
from filelock import FileLock

if(len(sys.argv) != 4):
    print("INCORRECT NUMBER OF ARGUMENTS PASSED.\nEXITING NOW.")
    exit()

dstFile = sys.argv[1]
srcFile = sys.argv[2]
operCode = sys.argv[3]
print("DESTINATION FILE: {}\nSOURCE FILE: {}\nOPERATION CODE: {}\n".format(dstFile, srcFile, operCode))

if operCode not in ['0', '1', '2']:
     print("Sorry! That operation code is invalid!")
     exit()

if os.path.isdir(srcFile):
    print("INPUT SOURCE FILE IS A DIRECTORY.\nEXITING NOW.")
    exit()
if os.path.isdir(dstFile):
    print("INPUT DESTINATION FILE IS A DIRECTORY.\nEXITING NOW.")
    exit()

if operCode in ['0', '1']:
    if not os.path.isfile(srcFile):
        print("SOURCE FILE NOT FOUND.\nEXITING NOW.")
        exit()

try:
    lockSrc = FileLock(srcFile + '.lock', timeout = 1)
    lockSrc.acquire()
    lockDst = FileLock(dstFile + '.lock', timeout = 1)
    lockDst.acquire()
    print("LOCKS ACQUIRED SUCCESSFULLY\n")
except:
    print("LOCKS COULD NOT BE ACQUIRED.\nEXITING NOW.")
    try:
        os.remove(srcFile + '.lock')
    except:
        pass
    try:
        os.remove(dstFile + '.lock')
    except:
        pass
    exit()

if operCode == '0':
    src = open(srcFile, 'r')
    dst = open(dstFile, 'a')
    dst.write(src.read())
    dst.close()
    src.close()
    print("FILE APPENDED SUCCESSFULLY.\n")

if operCode == '1':
    src = open(srcFile, 'r')
    dst = open(dstFile, 'w')
    dst.write(src.read())
    dst.close()
    src.close()
    print("FILE OVERWRITTEN SUCCESSFULLY.\n")


if operCode == '2':
    if os.path.isfile(srcFile):
        os.remove(srcFile)
    if os.path.isfile(dstFile):
        os.remove(dstFile)
    print("FILES DELETED SUCCESSFULLY.\n")

os.remove(srcFile + '.lock')
os.remove(dstFile + '.lock')

lockSrc.release()
lockDst.release()

print("OPERATION COMPLETE!")
