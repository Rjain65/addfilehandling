import os

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath,textToWrite):
    fileHandle = open(filePath,'w')
    fileHandle.write(textToWrite)
    fileHandle.close()

def readFile(filePath):
    if not fileExists(filePath):
        print ('the file', filePath ,'does not exists-cannot read it')

    fileHandle = open(filePath,'r')
    data = fileHandle.read()
    fileHandle.close()
    return data


fpath = "summ.txt"


if not fileExists:
    sum1 = 0.0
while True:
    psum = float(readFile(fpath))
    sum1 = input("write your number to add")
    try:
        sum1=  float(sum1)
    except :
        print("write a number idiot")
        continue
    
    if sum1 == 0:
        break
    sum1 = psum + sum1
    print(sum1)
    writeFile(fpath,str(sum1))
    


    
