#!/bin/bash
# Launch the Telegram reaction bot
set -e
source "$(dirname "$0")/venv/bin/activate"
python reactionbot.py

