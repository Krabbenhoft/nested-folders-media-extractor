#!/usr/bin/python3

from pathlib import Path
import shutil

def getSubfolders(inputFolder):
    return [item.resolve() for item in inputFolder.iterdir() if item.is_dir()]
    
def recursiveFolders(inputFolder):
    totalList = []
    currentList = getSubfolders(inputFolder)
    if(len(currentList) == 0):
        return []
    else:
        totalList.extend(currentList)
        for folder in currentList:
            totalList.extend(recursiveFolders(folder))
            
    return totalList

inputPath = Path('input')
outputPath = Path('output')
allPaths = recursiveFolders(inputPath)

for path in allPaths:
    currentSongs = [item.resolve() for item in path.iterdir() if not item.is_dir() and item != None]
    print(currentSongs)
    for song in currentSongs:
        shutil.copy(song, outputPath)