# linux-wallpaper-engine
### this app allows for simple video wallpapers on X11 based Linuxachunes 
## compadability 
- requires X11 based system
- works with polybars rounded corners
- works with picoms blur

## requirements
- python 3^ 
    - os
    - screeninfo 
    - flask
    - flask_cors
- npm 
    - electron
    - child_process
- packages
    - xwinwrap
    - mpv
    - xrandr
    - git
## Build from source 
```
git clone https://github.com/9jh1/linux-wallpaper-engine
cd linux-wallpaper-engine
./run_dev.sh
```
## ToDo
- remove need for screeninfo module
- add advanced settings menu