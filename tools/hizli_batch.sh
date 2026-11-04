#!/bin/bash
# Deney: her videoya 22:45 deneme Reels (stil rotasyonu). Idempotent: public/hizli/<tarih>.mp4 HEAD'de varsa atlar.
set -u
R=/home/claude/paranin-dili; S=/home/claude/pd_work/hz_src; O=/home/claude/pd_work/hz_out
export PD_WORK=/home/claude/pd_work WHISPER_MODEL=/root/models/whisper-turbo
mkdir -p $S $O $R/public/hizli
while IFS=$'\t' read -r -u3 d src st bas; do
  [ -n "${ONLY:-}" ] && [ "$d" != "$ONLY" ] && continue
  out=public/hizli/$d.mp4
  if git -C $R cat-file -e HEAD:$out 2>/dev/null; then echo "SKIP $d"; continue; fi
  n=$(basename $src)
  [ -s $S/$n.mp4 ] || git -C $R show HEAD:public/$src.mp4 > $S/$n.mp4
  python3 $R/tools/hizli.py $S/$n.mp4 $O/$d.mp4 --stil $st --baslik "$bas" > $O/$d.log 2>&1 || { echo "FAIL $d"; tail -3 $O/$d.log; continue; }
  sz=$(stat -c %s $O/$d.mp4)
  if [ $sz -gt 95000000 ]; then echo "TOO BIG $d $sz"; continue; fi
  cp $O/$d.mp4 $R/$out; cp $O/$d.mp4.json $R/public/hizli/$d.json
  (cd $R && git add $out public/hizli/$d.json && git commit -qm "hizli deneme $d ($st)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01653SBEUtYBTraJFkbppWCe" && git push -q && git update-index --skip-worktree $out && rm -f $out)
  echo "OK $d $st $(git -C $R rev-parse HEAD) $(tail -1 $O/$d.log)"
  rm -f $S/$n.mp4
done 3< <(tail -n +2 $R/videos/_deney_hizli.tsv)
