#!/bin/bash

rm /tmp/updates
checkupdates > /tmp/updates

if [[ -s /tmp/updates ]];then
    echo ""
else
    echo "There are no updates" > /tmp/updates
fi;

action=$(yad --button gtk-apply:0 \
	--button gtk-cancel:1 \
	--text-info \
	--geometry=350x300+800+20 \
	--class "YADWIN" \
    --filename=/tmp/updates)
ret=$?

# GTK-APPLY:0 - Run Update
if [[ $ret -eq 0 ]];then
	xfce4-terminal --command "pacaur -Syu" -T "Menu Update" --geometry=80x20+1272+25
fi
