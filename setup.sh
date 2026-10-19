#!/usr/bin/env bash
# One-time setup in a fresh cloud session (~3-6 min). Safe to re-run.
set -e
cd "$(dirname "$0")"
pip install --quiet --break-system-packages faster-whisper num2words scipy numpy 2>&1 | tail -1 || true
M=${WHISPER_MODEL:-$HOME/models/whisper-turbo}
if [ ! -s "$M/model.bin" ]; then
  mkdir -p "$M"
  BASE=https://github.com/blodym4ry/paranin-dili/releases/download/models-v1
  for f in config.json preprocessor_config.json tokenizer.json vocabulary.json; do curl -sSLf -o "$M/$f" "$BASE/$f"; done
  rm -f "$M/model.bin"
  for p in 00 01; do curl -sSLf "$BASE/model.bin.part$p" >> "$M/model.bin"; done
  echo "whisper model: $(du -h "$M/model.bin" | cut -f1)"
fi
# warm the HyperFrames CLI cache
npx --yes hyperframes@0.8.174 --version >/dev/null 2>&1 || true
command -v ffmpeg >/dev/null || { echo "ffmpeg missing"; exit 1; }
ls /opt/pw-browsers/chromium-1194/chrome-linux/chrome >/dev/null 2>&1 || echo "WARN: chromium-1194 not found; set HYPERFRAMES_BROWSER_PATH"
git config user.name >/dev/null || git config user.name "paranin-dili-bot"
git config user.email >/dev/null || git config user.email "bot@paranin-dili.local"
echo SETUP_OK
