from .monitors import get_single_res_info, get_full_res, get_monitor_names
from .dir import get_video_info
import os

def set_background(monitor="both",path="",audio_level=0): 
    os.system("killall -q xwinwrap")
    videoInfo = get_video_info(path)
    vWidth = videoInfo[1][0]
    vHeight = videoInfo[1][1]
    screenInfo = get_full_res()
    #toggles
    videoOrientation = ""
    videoPos = ""
    screenPos = ""
    command =  ""
    if vHeight < vWidth: 
        # video is horisontal
        videoOrientation = "horizontal"
    elif vHeight > vWidth:
        videoOrientation = "vertical"
    else:
        videoOrientation = "square"
    if monitor == "both": 
        screenPos = f"{screenInfo[0]}x{screenInfo[1]}+0+0"
    if videoOrientation == "horizontal": 
        videoPos = f"{vWidth}x{vHeight}+{int(vWidth/2)}+0"
    command = f"xwinwrap -g {screenPos} -ni -s -nf -ov -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={videoPos} --loop --no-border --video-align-x=1 --video-zoom=1 {path} -wid WID"
    os.system(command)