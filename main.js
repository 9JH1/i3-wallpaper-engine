const { app, BrowserWindow, Notification, ipcMain } = require('electron')
const path = require("path");
const { spawn } = require('child_process');
const fs = require('fs');
let startTime = null;
let appStartTime = null;
let appObj = "";

const restartApp = () => {
    app.relaunch()
    app.exit(0); // Exit the current instance of the app
    getData("/off")
    const errorMessage = new Notification({
        title: "restarting",
        body: "app restarting",
        icon: "icon.ico",
    })
    errorMessage.show()
};

function getData(endpoint) {
    return fetch(`http://127.0.0.1:22301${endpoint}`)
        .then((res) => res.text())
        .catch((error) => { });
}
async function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 500,
        minHeight: 500,
        minWidth: 800,
        maxHeight: 500,
        maxWidth: 800,
        autoHideMenuBar: true,
        webPreferences: {
            nodeIntegration: true,
            enableMainProcessInspector: true,
            contextIsolation: false,
            ipcMain: true
        },
        transparent:true,
        frame:false,
        icon: path.join(__dirname, 'icon.ico'),
    })

    mainWindow.loadFile('frontend/index.html')
}
app.setAppUserModelId("i3-wallpaper-engine")
app.whenReady().then(() => {
    (async () => {
        function mainApp() {
            startTime = Date.now();
            let child = spawn("python", [`${path.join(__dirname, "backend/main.py")}`], {
                detached: true,
                stdio: "ignore",
            })
            child.once('spawn', () => {
                const awaitServer = setInterval(() => {
                    console.log("probing");
                    (async () => {
                        appObj = await getData("");
                        if (appObj != undefined) {
                            awaitServer.close()
                            try {
                                createWindow()

                                appStartTime = Date.now();
                                console.log(`server took ${(Date.now() - startTime) / 1000}s to launch`);
                            } catch {

                                console.log("massive error");
                                const errorMessage = new Notification({
                                    title: "Error",
                                    body: "app couldn't initialize",
                                    icon: "icon.ico",
                                })
                                errorMessage.show();
                                getData("/off")
                                app.quit();
                            }
                        }
                    })();
                }, 1000)
            });
            child.on("exit", () => {
                console.log("server crashed")
                app.quit()
            })
        }
        if (await getData("")) {
            console.log("server on")
            while (await getData("")) {
                
                getData("/off");
                console.log("turning off")
            }
            mainApp()
        } else {
            mainApp()
        }
    })();
    app.on("before-quit", () => {
        getData("/off");
        console.log(`application open for ${(Math.floor((Date.now() - appStartTime) / 1000)/60)}m`);
    });
})
app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') {
        app.quit()
    }
});
ipcMain.on('restart', () => {
    restartApp();
});