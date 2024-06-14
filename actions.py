import os
import webbrowser
import subprocess

def perform_action(command):
    print(f"执行命令: {command} (Performing command: {command})")
    if "打开摄像头" in command or "opencamera" in command:
        subprocess.run(["start", "microsoft.windows.camera:"], shell=True)
    elif "打开音乐播放器" in command or "openmusicplayer" in command:
        subprocess.run(["start", "wmplayer"], shell=True)
    elif "打开记事本" in command or "opennotepad" in command:
        subprocess.run(["notepad"], shell=True)
    elif "搜索" in command or "search" in command:
        search_term = command.split("搜索")[1].strip() if "搜索" in command else command.split("search")[1].strip()
        search_url = f"https://www.baidu.com/s?wd={search_term}"
        webbrowser.open(search_url)
    else:
        print("未识别的命令 (Unrecognized command)")
    return {"status": "success", "command": command}
