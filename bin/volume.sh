#!/bin/sh

VOL=`/home/j/bin/pacvol.sh display | sed "s/[^1-9]//" | sed "s/%//"`
OUT=`yad --text="Volume" \
	 	--scale \
	 	--value $VOL \
	 	--button gtk-ok:0 \
		--buttons-layout center \
		--geometry=85x200+1000+20 \
	 	--class "YADWIN" \
 		--vertical \
 		--text-align center`

# GTK-OK - Set volume
if [[ $? -eq 0 ]];then
  amixer set Master $OUT%
fi
