from screeninfo import get_monitors

def getFullResInfo(): 
    full_list = {}
    for m in get_monitors():
        monitor = str(str(str(m).split("(")[1]).replace(")","")).split(",")
        for item in monitor: 
            full_list[item.split("=")[0].replace(" ","")] = item.split("=")[1].replace(" ","")
    return full_list
def getFullRes():
    lists = getFullResInfo()
    return [int(lists["width"]),int(lists["height"])]
print(getFullRes())
