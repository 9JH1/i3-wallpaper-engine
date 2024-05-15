const videos = document.getElementById("videos"); 
async function getData(endpoint) {
    return fetch(`http://127.0.0.1:22301${endpoint}`)
        .then((res) => res.json())
        .catch((error) => { });
}

function setInfoBoard(text){ 
    const info = document.getElementById("status")
    info.innerText = text;
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
                elementTwo.style.background = "green";
            })
            element.style.background = "red";
        })
    })
})()