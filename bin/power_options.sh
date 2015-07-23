#! /bin/bash

action=$(yad --entry --title "System Logout" \
    --button="gtk-ok:0" --button="gtk-close:1" \
    --geometry=x+y+$X+$Y \
    --class "YADWIN" \
    --text "Choose action:" \
    --entry-text \
    "Power Off" "Reboot" "Suspend" "Lock" "Exit")
ret=$?

# Put lock in it's own function to work
function lock {
    #scrot /tmp/screenshot.png
    #convert /tmp/screenshot.png -blur 0x5 /tmp/screenshotblur.png
    #eval exec i3lock -i /tmp/screenshotblur.png && sleep 1
    bash /home/j/bin/i3lock.sh
}

case $action in
    Power) 
	    systemctl poweroff 
	    ;;
    Reboot) 
	    systemctl reboot 
	    ;;
    Suspend) 
	    lock && systemctl suspend 
	    ;;
    Lock) 
	    lock
	    ;;
    Exit)
	    i3-msg exit 
	    ;;
    *) 
	    exit 1
esac
