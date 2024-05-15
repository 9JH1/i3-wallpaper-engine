const videos = document.getElementById("videos"); 
const monitors = document.getElementById("monitors");
async function getData(endpoint) {
    return fetch(`http://127.0.0.1:22301${endpoint}`)
        .then((res) => res.json())
        .catch((error) => { });
}

function setInfoBoard(){ 
    const info = document.getElementById("status")
    let infoText = "Video: "
    let monitorCount = 0
    let monitorName = ""
    let command = "/set/"
    let commandPath = ""

    monitors.querySelectorAll(".monitor-item-real").forEach(element =>{ 
        if(element.classList.contains("monitor-item-real-active")){ 
            monitorCount +=1;
            monitorName = element.innerText;
        }
    })
    videos.querySelectorAll(".video-item-real").forEach(element=>{
        if(element.style.background == "var(--selected)"){
            infoText += element.getElementsByClassName("title")[0].innerText
            commandPath = element.getElementsByClassName("title")[0].innerText
        }
    })
    if(monitorCount == 2){ 
        infoText += " on both monitors"
        command += "both"
    } else if (monitorCount == 1) {
        infoText += ` on ${monitorName}`
        command += monitorName
    } else { 
        infoText += " select a monitor"
    }
    info.innerText = infoText;
    command += commandPath
    getData(command)
    return true
}

(async ()=>{
    const files = await getData('/get_videos')
    videos.innerHTML = ""
    files.forEach(element => {
        const nc = document.createElement("button");
        nc.classList.add("video-item-real");
        nc.innerHTML = `
        <video src="${element}" class="thumbnail"></video>
        <p class="title">${element}</p>
        <p class="duration">00:25:00</p>
        
        `
        videos.appendChild(nc)
        
    });
    videos.querySelectorAll(".video-item-real").forEach(element=>{
        element.addEventListener("click",()=>{
            videos.querySelectorAll(".video-item-real").forEach(elementTwo =>{ 
                elementTwo.style.background = "var(--text)";
            })
            element.style.background = "var(--selected)";
            setInfoBoard()
        })
    })
})();

(async ()=>{
    const monitor = await getData("/get_monitors"); 
    console.log(monitor)
    monitor.forEach(element =>{
        const nc = document.createElement("button");
        nc.classList.add("monitor-item-real");
        nc.innerHTML = element
        monitors.appendChild(nc);
    })
    monitors.querySelectorAll(".monitor-item-real").forEach(element=>{
        element.addEventListener("click",()=>{
            element.classList.toggle("monitor-item-real-active")
            setInfoBoard()
        })
    })
})()