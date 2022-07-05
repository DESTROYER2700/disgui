import time
import requests 
A = 1
while True:
    payload = {
    'content': A
    }

    header = {
    'authorization': 'mfa.C4HlFtD1-lgy2RWAp5s_YucbmMmMi5AfZ92GDmSRwtnMZsz08GIzl_XbRNOwzY4zTIn90sMYiFmd9sqx6NN-'
    }

    # https://discord.com/api/v9/channels/882690794060918834/messages
    r = requests.post("https://discord.com/api/v9/channels/882690794060918834/messages", data=payload, headers=header )
    print(A)
    time.sleep(60)
    A = A + 1