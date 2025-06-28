#!/bin/bash
# Script to set up the Telegram reaction bot environment
# Expects API_ID, API_HASH and PHONE_NUMBER environment variables

set -e

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

mkdir -p sessions tdatas logs

if [[ -n "$API_ID" && -n "$API_HASH" && -n "$PHONE_NUMBER" ]]; then
  cat > sessions/account.json <<EOC
{
    "api_id": "$API_ID",
    "api_hash": "$API_HASH",
    "phone_number": "$PHONE_NUMBER"
}
EOC
  echo "Created sessions/account.json"
else
  echo "Provide API_ID, API_HASH and PHONE_NUMBER environment variables to create a session config."
fi

echo "Setup complete. Run: python reactionbot.py"
