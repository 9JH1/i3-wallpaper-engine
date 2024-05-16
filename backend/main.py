from res.scrape import networkBypass
from res.monitors import get_monitor_names, get_full_res
from res.dir import get_video_info 
from res.dir import get_videos_grep as get_videos
import flask 
import flask_cors
import os
import subprocess
import signal



app = flask.Flask(__name__)
CORS = flask_cors.CORS(app)
@app.route("/get_videos/<path:paths>")
def return_videos(paths="/"):
    return get_videos(f"/{paths.replace("rootFind22301","")}")
@app.route("/get_videos_root")
def return_videos_root():
    return get_videos("/")
@app.route("/get_monitors")
def return_monitors(): 
    return get_monitor_names()
@app.route("/")
def show_root():
    return "i3-wallpaper-engine"






@app.route("/set/<monitors>/<path:paths>")
def set_background(monitors="both",paths="",audio_level=0):
    print(paths)
    paths = f"/{paths}"
    paths = paths.replace("%20"," ")
    os.system("killall -q xwinwrap")
    videoInfo = get_video_info(paths)
    vWidth = videoInfo[1][0]
    vHeight = videoInfo[1][1]
    print(vWidth)
    screenInfo = get_full_res()
    #toggles
    videoOrientation = ""
    videoPos = ""
    screenPos = ""
    command =  ""
    videoZoom = "1" # ~2.661
    if vHeight < vWidth: 
        videoOrientation = "horizontal"
    elif vHeight > vWidth:
        videoOrientation = "vertical"
    else:
        videoOrientation = "square"
    if monitors == "both": 
        screenPos = f"{int(screenInfo[0]/2)*2}x{screenInfo[1]}+0+0"
    else:
        screenPos = f"{int(screenInfo[0]/2)}x{screenInfo[1]}+0+0"
    if videoOrientation == "horizontal": 
            videoPos = f"{vWidth}x{vHeight}+{int(vWidth/2)}+0"
    elif videoOrientation == "vertical":
        videoPos = f"0x0+0+0"

    command = f"xwinwrap -g {screenPos} -ni -s -nf -ov -argb -- mpv --mute=yes --no-audio --no-osc --no-osd-bar --quiet --screen=1 --geometry={videoPos} --loop --no-border --video-align-x=0 --video-align-y=0 --video-zoom={videoZoom} '/{paths}' -wid WID"
    os.system(command)
    set_background(monitor=monitors,path=f'/{paths}')
    return "set"

@app.route("/video_info/<path:paths>")
def return_video_info(paths): 
    return get_video_info(f"/{paths}")
@app.route(f"/off")
def stop_server():
    os.system("killall -q xwinwrap")
    os.kill(os.getpid(), signal.SIGINT)
    return flask.jsonify({"success": True, "message": "Server is shutting down..."})
if __name__ == "__main__":
    app.run(port=22301)