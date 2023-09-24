import os,platform
os.system('git pull')
 
Danish=platform.architecture()[0]
if Danish=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif Danish=="64bit":
     __import__("Danish")
