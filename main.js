const { app, BrowserWindow, Notification, ipcMain } = require('electron')
const path = require("path");
const { execFile } = require('child_process');
const fs = require('fs');
let startTime = null;
let appObj = "";
let jsonObj;
let jsonObjAccent = "";
let jsonObjBackground = "";
let jsonData;

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
        icon: path.join(__dirname, 'icon.ico'),
    })

    mainWindow.loadFile('backend/templates/frontend/index.html')
}
app.setAppUserModelId("i3-wallpaper-engine")
app.whenReady().then(() => {
    (async () => {

        createWindow()
        function mainApp() {
            startTime = Date.now();
            let child = execFile("python " + [path.join(__dirname, "backend/main.py")], {
                detached: true,
                stdio: "ignore",
            })
            
            child.unref();
            child.once('spawn', () => {
                const awaitServer = setInterval(() => {
                    (async () => {
                        appObj = await getData("");
                        if (appObj == undefined) {
                            awaitServer.close()
                            appObj = JSON.parse(appObj)
                            try {
                                createWindow()
                                console.log(`server took ${(Date.now() - startTime) / 1000}s to launch`);
                            } catch {

                                console.log("massive error in themes file, i dunno how to fix it good luck");
                                const errorMessage = new Notification({
                                    title: "Error",
                                    body: "app couldn't initialize due to broken themes file",
                                    icon: "icon.ico",
                                })
                                errorMessage.show();
                                console.log("");
                                console.log(jsonObj);
                                console.log("");
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
                console.log("turning off ")
            }
            mainApp()
        } else {
            mainApp()
        }
    })();
    app.on("before-quit", () => {
        getData("/off");
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