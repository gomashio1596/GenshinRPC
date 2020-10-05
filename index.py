import time
from typing import Optional

import psutil
from pypresence import Presence

def get_process_by_name(name: str, path_contains: Optional[str] = None) -> Optional[psutil.Process]:
    for process in psutil.process_iter(['name','exe','pid','create_time']):
        if process.info['name'] == name and path_contains in process.info['exe']:
            return process
    return None

client_id = '761114571770560522'

while True:
    print('原神の起動を待っています...')
    process = get_process_by_name('GenshinImpact.exe','Genshin Impact Game')
    while process is None:
        process = get_process_by_name('GenshinImpact.exe','Genshin Impact Game')
        time.sleep(1)
    print('原神の起動を確認しました。RPCに接続します...')

    rpc = Presence(client_id)
    rpc.connect()
    print('接続完了')
    rpc.update(
        pid=process.info['pid'],
        start=process.info['create_time'],
        large_image='genshin',
        large_text='原神',
        details='原神をプレイ中',
        state='テイワット大陸'
    )

    while True:
        time.sleep(15)
        process = get_process_by_name('GenshinImpact.exe','Genshin Impact Game')
        if process is None:
            break
    print('原神の終了を検知しました。PRCから切断します...\n')
    rpc.close()