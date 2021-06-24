import time
from datetime import datetime as dt

pages_list = [
    'https://www.youtube.com',
    'youtube.com',
    'www.youtube.com'
    'facebook.com',
    'instagram.com',
    'www.instagram.com'
]

start_h = 8
end_h = 12


local_host = '127.0.0.1'
hosts_file_wn = r"C:\Windows\System32\drivers\etc\hosts" 
hosts_file_unix = "/etc/hosts"
hosts = hosts_file_wn #Libre de cambiar en esta linea para usar en Linux/Mac o Windows

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_h) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_h):
        with open(hosts, 'r+') as file:
            content = file.read()
            for i in pages_list:
                if i in content:
                    pass
                else:
                    file.write(local_host + ' ' + i +'\n')
        print("running...")            
    else:
        with open(hosts,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in pages_list):
                    file.write(line)
            file.truncate()
        print("sleep...")               
    time.sleep(1)

