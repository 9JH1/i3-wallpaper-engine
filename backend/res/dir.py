import os 
import subprocess

def getVideos():
    listOfVids = []
    res = str(subprocess.run(["find","/"],capture_output=True).stdout).strip().replace("b'","").replace("'","").split("\\n")
    for value in res: 
        if value.endswith("mp4"):
            listOfVids.append(value)
    return listOfVids


def getVideoLength(path): 
    return "info of "+ path
    
def getVideoDimensions(path):
    return "width and length of " + path

