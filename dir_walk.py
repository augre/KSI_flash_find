import os

##
rootdir =os.path.normpath('C:/Users/Z3 Demo/Desktop/KSI-Arrow')
##look_for  = "NAND:  1024 MiB"
look_for  = "NAND:  256 MiB"
count=0

for subdir, dirs, files in os.walk(rootdir):
    for file in files: 
##        if file.find("xls")!=-1 or file.find("pdf")!=-1 or file.find("jpg")!=-1:
##            pass
##        else:
            f=open(os.path.join(subdir, file),'r')
            text=f.read()
            if text.find(look_for)!=-1:
                print "not passed"
                print os.path.join(subdir, file)
                count=count+1
            

print "Count: ", count


##count=0
##for subdir, dirs, files in os.walk(rootdir):
##    for file in files:
##        count=count+1
##
##print count
