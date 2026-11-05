#!/bin/bash
# İlk 4 saniye: animasyon videosuna t=0 boom + 2.1 sn whoosh ekler (görüntü kopyalanır).
in=$1; out=$2; S=/home/claude/pd_work/sfx
ffmpeg -v error -y -i "$in" -i $S/boom.mp3 -i $S/whoosh_bas.mp3 -filter_complex \
 "[1:a]volume=-7dB[b];[2:a]volume=-12dB,adelay=2100|2100[w];[0:a][b][w]amix=inputs=3:normalize=0:duration=first,alimiter=limit=0.95[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 160k -ar 48000 -movflags +faststart "$out"
