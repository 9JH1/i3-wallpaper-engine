import os 
import subprocess
from moviepy.editor import VideoFileClip

def get_video_info(file_path):
    try:
        video = VideoFileClip(file_path)
        duration = video.duration
        width, height = video.size
        video.close()
        return [duration, [width, height]]
    except Exception as e:
        return None, None

def get_videos(path):
    listOfVids = []
    res = str(subprocess.run(["find",path],capture_output=True).stdout).strip().replace("b'","").replace("'","").split("\\n")
    for value in res: 
        if value.endswith("mp4"):
            listOfVids.append(value)
    return listOfVids
def get_videos_grep(path):
    try:
        result = subprocess.run(f"find {path} | grep '.mp4$'", shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return []