from screeninfo import get_monitors

def get_full_res_info(): 
    full_list = []
    for m in get_monitors():
        monitor_info = str(m).split(", ")
        monitor_dict = {}
        for item in monitor_info:
            key, value = item.split("=")
            monitor_dict[key.strip()] = value.strip()
        full_list.append(monitor_dict)
    return full_list

def get_full_res():
    info = get_full_res_info()
    total_width = sum([int(monitor["width"]) for monitor in info])
    max_height = max([int(monitor["height"]) for monitor in info])
    return [total_width, max_height]

def get_monitor_names():
    monitors = get_monitors()
    names = [f"{monitor.name}" for monitor in monitors]
    return names
