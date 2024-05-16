const videos = document.getElementById("videos"); 
const monitors = document.getElementById("monitors");


function cutOutPutText(text, cutNum) {
    let output = "";
    for (let i = 0; i < cutNum; i++) {
        if( i < text.length){
            output += text[i];
        }
    }
    if(cutNum < text.length){
        return output + "...";
    } else {
        return output;
    }
}

async function getData(endpoint) {
    return fetch(`http://127.0.0.1:22301${endpoint}`)
        .then((res) => res.json())
        .catch((error) => { });
}
function removeFileNameFromPath(path) {
    // Split the path by '/'
    const pathParts = path.split('/');
    
    // Remove the last part (the filename)
    pathParts.pop();
    
    // Join the remaining parts back into a path string
    const newPath = pathParts.join('/');
    
    return newPath;
}
let pathOf = "rootFind22301"
let countCommand = 0
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
            commandPath = element.getElementsByClassName("title")[0].dataset.src
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
    command += commandPath.replaceAll(" ","%20")
    getData(command)
    countCommand++
    info.innerText = countCommand
    return true
}
function setThings() {
    (async () => {
        const files = await getData(`/get_videos/${pathOf}`);
        files.forEach(async element => {
            const nc = document.createElement("button");
            nc.classList.add("video-item-real");
            nc.innerHTML = `
                <video src="${element}" data-src="${element}" class="thumbnail"></video>
                <p class="title" data-src="${element}">${cutOutPutText(element, 500)}</p>
                <p class="duration">
                </p>
            `;
            videos.appendChild(nc);
        });

        // Attach event listener outside the loop
        videos.querySelectorAll(".video-item-real").forEach(element => {
            element.addEventListener("click", () => {
                videos.querySelectorAll(".video-item-real").forEach(elementTwo => {
                    elementTwo.style.background = "var(--text)";
                });
                element.style.background = "var(--selected)";
                setInfoBoard();
                
            });
            function handleIntersection(entries, observer) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const thumbnail = entry.target.querySelector(".thumbnail");
                        const duration = entry.target.querySelector(".duration");
                        
                        if (thumbnail && duration) {
                            thumbnail.src = thumbnail.dataset.src;
                            (async () => {
                                const fileInfo = await getData(`/video_info/${thumbnail.dataset.src}`);
                                if(fileInfo != undefined){  
                                    duration.innerText = `${fileInfo[0]} | ${fileInfo[1][0]} x ${fileInfo[1][1]} `
                                }
                            })()
                        }
                    }
                });
            }
        
            // Function to handle when the target element exits the viewport
            function handleExit(entries, observer) {
                entries.forEach(entry => {
                    if (!entry.isIntersecting) {
                        element.getElementsByClassName("thumbnail")[0].src = ""
                        
                    }
                });
            }
        
            // Create an Intersection Observer
            const observer = new IntersectionObserver(handleIntersection);
            const exitObserver = new IntersectionObserver(handleExit);
        
            // Specify the target element
            const target = element;
        
            // Start observing the target element
            observer.observe(target);
            exitObserver.observe(target);
        });
    })();
}

(async ()=>{
    const monitor = await getData("/get_monitors"); 
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
setThings()

function handleFolderSelection(event) {
    const fullPath = event.target.files[0].path;
    pathOf = removeFileNameFromPath(fullPath)
    setThings()
}