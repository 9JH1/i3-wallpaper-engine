from .monitors import get_single_res_info, get_full_res, get_monitor_names
import os

def set_background(monitor="both", path="", audio_level="", speed="", scale=""):
    path = path.replace("%20", " ")
    os.system("killall -q xwinwrap")

    if monitor != "both":
        monitor_names = get_monitor_names()
        index_of_monitor = monitor_names.index(monitor)
        sizes = get_single_res_info(monitor_names[0])

        # Determine if scaling is needed and calculate scaling factors
        vWidth, vHeight = 1080, 1080  # Assuming default video dimensions
        sWidth, sHeight = sizes['width'], sizes['height']
        scale_width = vWidth / sWidth
        scale_height = vHeight / sHeight

        if index_of_monitor == 1:
            command = f"xwinwrap -g {sizes['width']}x{sizes['height']}+{sizes['width']}+0 -ni -s -nf -ov -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={sizes['width']}x{sizes['height']}+0+0 --loop --no-border --video-align-x=1 --video-zoom=1 {path} -wid WID"
        else:
            command = f"xwinwrap -g {sizes['width']}x{sizes['height']} -ni -s -nf -ov -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={sizes['width']}x{sizes['height']}+{sizes['height']}+0 --loop --no-border --video-align-x=1 --video-zoom=1 {path} -wid WID"

        # Adjust the command based on scaling factors
        if scale_width != 1.0 or scale_height != 1.0:
            command += f" --video-zoom={min(scale_width, scale_height)}"

    else:
        full_res = get_full_res()
        sizes = get_single_res_info(get_monitor_names()[0])

        # Determine if scaling is needed and calculate scaling factors
        vWidth, vHeight = 1080, 1080  # Assuming default video dimensions
        sWidth, sHeight = sizes['width'], sizes['height']
        scale_width = vWidth / sWidth
        scale_height = vHeight / sHeight

        command = f"xwinwrap -g {full_res[0]}x{full_res[1]} -ni -s -nf -b -un -ov -fdt -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={int(full_res[0] / 2)}x{full_res[1]}+100+10% --loop --no-border --video-align-x=1 --video-zoom=1 {path} -wid WID"

        # Adjust the command based on scaling factors
        if scale_width != 1.0 or scale_height != 1.0:
            command += f" --video-zoom={min(scale_width, scale_height)}"

    os.system(command)
def compile(vWidth, vHeight, sWidth, sHeight): 
    # Figure out if it needs scaling
    if vWidth >= sWidth: 
        print("width positive scale")
    else:
        print("width negative scale")

    if vHeight >= sHeight: 
        print("height positive scale")
    else:
        print("height negative scale")

    # Figure out orientation 
    if vWidth > vHeight:
        print("video is horizontal")
    elif vWidth < vHeight: 
        print("video is vertical")
    else:
        print("video is a square")

    print(f"height requires {vHeight / sHeight}x scale")
    print(f"width requires {vWidth / sWidth}x scale")

def set_full_background(videoWidth,videoHeight,videoPath,setMode="fill",audioLevel=0,scaleAxis="y",monitor='both',screenWidth=get_full_res()[0],screenHeight=get_full_res()[1]):
    audioLevelArgs = "--mute=yes --no-audio"
    scaleAxisArgs = "--video-align-x"
    command = "xwinwrap -g {screenWidth}x{screenHeight}+{screenPlusHeight}+{screenPlusWidth} -ni -s -nf -ov -argb -- mpv {audioLevelArgs} --no-osc --no-osd-bar --quiet --screen={screen} --geometry={videoWidth}x{videoHeight}+{videoPlusWidth}+{videoPlusHeight} --loop --no-border --video-align-{videoAlignAxis}={videoAlignAxisScale} --video-zoom={videoZoom} {path} -wid WID"
    if(monitor != "both"):
        monitor =int(get_monitor_names.index(monitor))
    if(audioLevel !=0 ): 
        audioLevelArgs = "--mute=no"
    else: 
        audioLevelArgs = f"--volume={audioLevel}"
    if(setMode="fill"):
        command = command.format(
            screenWidth,
            screenHeight, 
            0,
            0,
            audioLevelArgs, 
            monitor,
            videoWidth, 
            videoHeight, 
        )


    