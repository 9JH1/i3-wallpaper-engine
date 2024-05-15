const monitors = document.getElementById("monitors"); 
function getData(endpoint) {
    return fetch(`http://127.0.0.1:22301${endpoint}`)
        .then((res) => res.text())
        .catch((error) => { });
}

(async ()=>{
    monitors.innerHTML = await getData("/");
})()