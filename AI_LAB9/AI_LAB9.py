import csv
import math
import copy

def Mod(file):
    valDict={}

    for row in file:
        if ''+row[1] in valDict:
            valDict[''+row[1]]+=1
        else:
            valDict[''+row[1]]=1

    maxKey=max(valDict, key=valDict.get)
    
    return float(maxKey)

def Med(file):
    rowList=[]

    for row in file:
        rowList.append(row[1])

    rowList=sorted(rowList)
    listLength=len(rowList)

    if listLength%2==0:
        midIndex=int((listLength-1)/2)

        return (float(rowList[midIndex])+float(rowList[midIndex+1]))/2
    else:
        return float(rowList[(listLength-1)/2])

def Average(file):
    avg=0
    i=1

    for row in file:
        if not i==1:
            avg+=float(row[1])
        i+=1

    return avg/i

def Delta(file):
    rowList=[]

    i=0

    for row in file:
        if not i==0:
            rowList.append(float(row[1]))

        i+=1

    return max(rowList)-min(rowList)

def ThreeParts(file):
    parts=[]

    columnList=[]

    for row in file:
        columnList.append(row[1])

    size=len(columnList)

    partSize=int(size/3)

    for j in range(3):
        partList=[]
        for i in range(int(partSize/3)):
            partList.append(columnList[partSize*j+i])
        parts.append(partList)

    return parts

def Disp(file):

    average=Average(file)

    columnList=[]

    i=0

    for row in file:
        if not i==0:
            columnList.append(float(row[1]))

        i+=1

    n=len(columnList)

    disp=0

    for i in range(n):
        disp+=((columnList[i]-average)**2)/(n-1)

    return math.sqrt(disp)

with open("16.csv", "r") as readFile:
    readed=csv.reader(readFile, delimiter=';')
    
    bruh=copy.copy(list(readed))

    print(f'Среднее значение столбика = {Average(bruh)}')
    print(f'Медиана столбика = {Med(bruh)}')
    print(f'Мода столбика = {Mod(bruh)}')
    print(f'Размах = {Delta(bruh)}')
    print(f'Дисперсия = {Disp(bruh)}')

    parts=ThreeParts(bruh)

    print('Разделение на части.')
    print(f'Часть 1: {parts[0]}')
    print(f'Часть 1: {parts[1]}')
    print(f'Часть 1: {parts[2]}')