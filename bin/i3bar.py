#!/usr/bin/env python

import subprocess
import sys
import json

conkyrc="/home/j/.i3/conkyrc"

print('{"version":1, "click_events": true }')
print('[')
print('[],')
sys.stdout.flush()
subprocess.Popen(["conky", "-d", "-c", conkyrc])

class Item:
    commands={}
    processes={}
    def __init__(self, commands):
        self.commands=commands
        self.processes={}
    def execute(self,button):
        if button in self.commands:
            self.processes[button]=subprocess.Popen(self.commands[button],stdout=subprocess.DEVNULL)
    def kill(self,button):
        self.processes[button].kill()
    def is_running(self,button):
        if button not in self.processes:
            return False
        process=self.processes[button]

        if process.poll()==None:
            return True
        return False

    def toggle(self,button):
        if self.is_running(button):
            self.kill(button)
        else:
            self.execute(button)


items={}
items["battery"]=Item(
            {
                1:["xfce4-terminal", "-H", "--command", "acpi -V", "-T", "System Information", "--geometry=80x20+1272+25"]
            }
        )
items["brightness"]=Item(
            {
                1:["bash", "/home/j/bin/brightness_change.sh"]
            }
        )
items["cpu"]=Item(
            {
                1:["xfce4-terminal", "-H", "--command", "top", "-T", "Process Monitor", "--geometry=100x30+1115+25"]
            }
        )
items["date"]=Item(
            {
                1:["yad", "--button", "gtk-ok:0", "--geometry=++1650+25", "--class", "YADWIN", "--calendar"]
            }
        )
items["disk"]=Item(
            {
                1:["xfce4-terminal", "-H", "--command", "pydf", "-T", "System Information", "--geometry=80x20+1272+25"]
            }
        )
items["net"]=Item(
            {
                1:["xfce4-terminal", "-H", "--command", "iftop -P -b -l -B", "-T", "Network Monitor", "--geometry=100x30+1115+25"]
            }
        )
items["power"]=Item(
            {
                1:["bash", "/home/j/bin/power_options.sh"]
            }
        )
items["updates"]=Item(
            {
                1:["bash", "/home/j/bin/check_updates_yad.sh"]
            }
        )
items["uptime"]=Item(
            {
                1:["xfce4-terminal", "-H", "--command", "archey", "-T", "System Information", "--geometry=80x20+1272+25"]
            }
        )
items["temp"]=Item(
            {
                1:["xfce4-terminal", "-H", "--command", "sensors", "-T", "System Information", "--geometry=80x20+1272+25"]
            }
        )
items["volume"]=Item(
            {
                1:["bash", "/home/j/bin/volume.sh"]
            }
        )

for i in sys.stdin:
    if i=="[\n":
        continue
    try:
        clickevent=json.loads(i.strip(',\\'))
        name=clickevent["name"]
        button=clickevent["button"]

        if name in items:
            item=items[name]
            if name != None:
                item.toggle(button)

    except TypeError as e:
        print(e)
        pass
    else:
        print('good')
        pass
