#!/bin/bash
LEVEL=`/home/j/bin/blevel.sh`
OUT=`yad --text="Brightness" --scale --value $LEVEL --button gtk-ok:0 --geometry=x200+1100+20 --class "YADWIN" --vertical --text-align center`
if [[ $? -eq 0 ]];then
  xbacklight -set $OUT
fi
