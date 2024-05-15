import os 
import subprocess

def getVideos():
    listOfVids = []
    res = str(subprocess.run(["find","/"],capture_output=True).stdout).strip().replace("b'","").replace("'","").split("\\n")
    for value in res: 
        if value.endswith("mp4"):
            listOfVids.append(value)
    return listOfVids


def getVideoInfo(path): 
    return "info of "+ path