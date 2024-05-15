from .monitors import get_single_res_info, get_full_res, get_monitor_names
import os
def set_background(monitor="both",path="",audio_level="",speed="",scale=""):
    command = ""
    path = path.replace("%20"," ")
    os.system("killall -q xwinwrap")
    if monitor !="both":
        indexOfMonitor = get_monitor_names().index(monitor)
        sizes = get_single_res_info(get_monitor_names()[0])
        if(indexOfMonitor == 1):
            command = f"xwinwrap -g {sizes['width']}x{sizes['height']}+{sizes['width']}+0 -ni -s -nf -ov  -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={sizes['width']}x{sizes['height']}+0+0 --loop --no-border --video-align-x=1 --video-zoom=1 {path} -wid WID"
        else:
            command = f"xwinwrap -g {sizes['width']}x{sizes['height']} -ni -s -nf -ov  -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={sizes['width']}x{sizes['height']}+{sizes['height']}+0 --loop --no-border --video-align-x=1 --video-zoom=1 {path} -wid WID"
    else:
        command = f"xwinwrap -g {get_full_res()[0]}x{get_full_res()[1]} -ni -s -nf -b -un -ov -fdt -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={int(get_full_res()[0]/2)}x{get_full_res()[1]}+100+10% --loop --no-border --video-align-x=1 --video-zoom=1 {path} -wid WID"
        print(get_full_res())
    os.system(command)