#!/bin/bash
# Aralık ana video bitirme: sfx + Ata HERO + kontrol kareleri + v2 (21:45) + hızlı (22:45) + commit/push. Metricool ayrı.
# kullanım: [NOAV=1] tools/aralik_bitir.sh <YYYY-MM-DD> <slug> <hizli_stil>
set -e
D=$1; S=$2; HS=$3; P=/home/claude/pd_work; A=$P/anim/$D; R=/home/claude/paranin-dili; SP=/tmp/claude-0/-home-claude/e7920022-8332-59f9-b10e-dcbfb990d4a4/scratchpad
export PD_WORK=$P
cd $R
bash tools/anim_sfx.sh $A/final.mp4 $A/sfx.mp4
if [ "$NOAV" = "1" ]; then mv $A/sfx.mp4 $A/out.mp4   # Ata onayı 6 Kas: 3, 4, 8 Ara avatarsız (sadece ses)
else python3 tools/anim_avatar.py $A/sfx.mp4 $S $A/words_trim.json $A/out.mp4; rm -f $A/sfx.mp4; fi
i=0; for t in 0.1 1.2 2.5 8 14 20 26 32 38 44 50 56; do ffmpeg -v error -y -ss $t -i $A/out.mp4 -frames:v 1 -vf scale=216:-1 $A/c_$(printf %02d $i).png; i=$((i+1)); done
ffmpeg -v error -y -i $A/c_%02d.png -vf tile=6x2 -frames:v 1 $SP/cs_$D.png; rm $A/c_*.png
python3 tools/v2kanca.py $A/final.mp4 $A/out.mp4 $P/aralik/v2/$D.mp3 $A/words_trim.json $P/aralik/v2_$D.mp4 $P/aralik/v2/$D.json
python3 tools/hizli.py $A/out.mp4 $P/aralik/hz_$D.mp4 --stil $HS | tail -1
cp $A/out.mp4 public/aralik/$D.mp4; cp $P/aralik/v2_$D.mp4 public/aralik/${D}_v2.mp4; cp $P/aralik/hz_$D.mp4 public/aralik/${D}_hz.mp4
git add public/aralik/$D.mp4 public/aralik/${D}_v2.mp4 public/aralik/${D}_hz.mp4
git commit -qm "Aralık: $D ana + v2 + hızlı ($S)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01653SBEUtYBTraJFkbppWCe"
git push -q 2>&1 | grep -vi warning || true
C=$(git rev-parse HEAD)
for f in $D ${D}_v2 ${D}_hz; do git update-index --skip-worktree public/aralik/$f.mp4; rm public/aralik/$f.mp4; done
echo "COMMIT $C"
