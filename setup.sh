#!/usr/bin/env bash
# One-time setup in a fresh cloud session (~3-6 min). Safe to re-run; run in background if your tool timeout is <10 min.
set -e
cd "$(dirname "$0")"
pip install --quiet --break-system-packages faster-whisper num2words scipy numpy 2>&1 | tail -1 || true
M=${WHISPER_MODEL:-$HOME/models/whisper-turbo}
# verified marker: a partial model.bin from a killed run must never be accepted
if [ -s "$M/model.bin" ] && [ ! -f "$M/model.bin.ok" ] && [ -s "$M/model.bin.sha256" ]; then
  (cd "$M" && echo "$(cat model.bin.sha256)  model.bin" | sha256sum -c - >/dev/null 2>&1) && touch "$M/model.bin.ok" || rm -f "$M/model.bin"
fi
if [ ! -f "$M/model.bin.ok" ]; then
  mkdir -p "$M/parts"
  BASE=https://raw.githubusercontent.com/blodym4ry/paranin-dili/models/whisper-turbo
  for f in config.json preprocessor_config.json tokenizer.json vocabulary.json parts.txt model.bin.sha256; do curl -sSLf --retry 3 -o "$M/$f" "$BASE/$f"; done
  # parallel part download (resumable: finished parts are kept), then atomic assemble
  xargs -P 6 -I{} sh -c '[ -f "'"$M"'/parts/{}.done" ] || { curl -sSLf --retry 3 -o "'"$M"'/parts/{}" "'"$BASE"'/{}" && touch "'"$M"'/parts/{}.done"; }' < "$M/parts.txt"
  rm -f "$M/model.bin.tmp"; for p in $(cat "$M/parts.txt"); do cat "$M/parts/$p" >> "$M/model.bin.tmp"; done
  if (cd "$M" && echo "$(cat model.bin.sha256)  model.bin.tmp" | sha256sum -c -); then
    mv "$M/model.bin.tmp" "$M/model.bin" && touch "$M/model.bin.ok" && rm -rf "$M/parts" && echo "model.bin: OK"
  else echo "whisper model checksum FAILED"; rm -f "$M/model.bin.tmp" "$M/parts"/*.done; fi
else echo "model.bin: OK (cached)"; fi
# warm the HyperFrames CLI cache
npx --yes hyperframes@0.8.174 --version >/dev/null 2>&1 || true
command -v ffmpeg >/dev/null || { echo "ffmpeg missing"; exit 1; }
ls /opt/pw-browsers/chromium-1194/chrome-linux/chrome >/dev/null 2>&1 || echo "WARN: chromium-1194 not found; set HYPERFRAMES_BROWSER_PATH"
git config user.name >/dev/null || git config user.name "paranin-dili-bot"
git config user.email >/dev/null || git config user.email "bot@paranin-dili.local"
echo SETUP_OK
