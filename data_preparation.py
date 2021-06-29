import os

num_faces = 10

os.mkdir("./Faces")
os.mkdir("./Faces/train")
os.mkdir("./Faces/test")
for i in range(num_faces):
    path = "./Faces/train/s"+str(i+1)
    os.mkdir(path)

dirlist = ["jpg-a", "jpg-b", "jpg-c", "jpg-d", "jpg-e"]

folderFileCount = [1]*num_faces

newPathTrain = "./Faces/train/"
newPathTest = "./Faces/test/"

for Dir in dirlist:
    path = "./" + Dir
    #print(path)
    files = os.listdir(path)
    for file in range(3*num_faces):
        src = path + "/" + files[file]
        #print("\t",src, end = "")
        folder_number = file//3
        #print("\t",folder_number, end = "")
        #print("\t",folderFileCount[folder_number])
        folder = "s"+str(folder_number + 1)+"/"
        newname = str(folderFileCount[file//3])+".jpg"
        #print("\t\t",folder,"\t",newname, end = "")
        folderFileCount[file//3] += 1
        dst = newPathTrain + folder + newname
        #print("\t",dst)
        os.replace(src, dst)

#print("\n")

testfiles = [str(i)+".jpg" for i in range(11,16)]

testfilecount = 1

for i in range(num_faces):
    folder = newPathTrain + "s" + str(i+1) + "/"
    for file in testfiles:
        src = folder+file
        newname = str(testfilecount) + ".jpg"
        testfilecount += 1
        dst = newPathTest + newname
        os.replace(src,dst)
        #print(src, "\t", dst)

