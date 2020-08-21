import os
import json
import subprocess

path = os.getcwd()

def start_player(peer, msg_id, token, pics, delay, play_list):
    animdata = {
        "peer": peer,
        "msg_id": msg_id,
        "token": token,
        "delay": delay,
        "pics": pics,
        "play_list": play_list
    }
    with open(os.path.join(path, "animdata"), 'w', encoding="utf-8") as data:
        data.write(json.dumps(animdata, ensure_ascii=False))
    subprocess.Popen(f"python3 {os.getcwd()}/ICAD/animplayer.py", shell=True)