import os
if(os.path.exists("demoFile.txt")):
   os.remove("demoFile.txt")
else:
    print("The file doesnot exist! ")
