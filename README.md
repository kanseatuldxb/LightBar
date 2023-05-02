# LightBar
```json
{"Body":{
   "FullName":"Ali",
   "PersonType":"Blacklisted",
   "AccessZone":"Full Access",
"PhotoFile":"<Base64 File>"

}
"Response":{
   "result":0,
   "message":"Record has been processed"
}
```
PersonType

WhiteList -> Normal
BlackList -> Blacklisted
VVIP -> VVIP

AccessZone

Zone1,Zone2,EntryGate
Zone 1, Zone 2, Full Access
````
   17  python run-soc.py
   18  clear
   19  sudo reboot
   20  ifconfig
   21  cd Module/
   22  python run-soc.py
   23  cd Module/
   24  ls
   25  nano run-soc.py
   26  python run-soc.py
   27  nano run-soc.py
   28  python run-soc.py
   29  nano run-soc.py
   30  python run-soc.py
   31  sudo nano /lib/systemd/system/blink.service
````
#systemd file
````
[Unit]
Description=Blink my LED
After=multi-user.target
User=tektron

[Service]
Restart=always
RestartSec=3
WorkingDirectory=/home/tektron/Module
ExecStart=/usr/bin/python3 /home/tektron/Module/run-soc.py

[Install]
WantedBy=multi-user.target

````
#systemd file setup
````
   32  sudo systemctl daemon-reload
   33  sudo systemctl enable blink.service
   34  sudo systemctl start blink.service
   35  sudo systemctl status blink.service
   36  ls
   37  pwd
   38  sudo nano /lib/systemd/system/blink.service
   39  sudo systemctl daemon-reload
   40  sudo systemctl start blink.service
   41  sudo systemctl status blink.service
   42  sudo pip install websocket-client
   43  sudo systemctl start blink.service
   44  history
   
````
