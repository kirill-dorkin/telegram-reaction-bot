import json
import asyncio
import logging
import random
from pathlib import Path

import typer
from pyrogram import Client, errors

from config import EMOJIS

app = typer.Typer(help="Simple interface to manage Telegram reaction accounts")

SESSIONS_DIR = Path("sessions")
LOGS_DIR = Path("logs")
SESSIONS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(filename=LOGS_DIR / "app.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


@app.command()
def add_account(api_id: int = typer.Option(..., prompt=True),
                api_hash: str = typer.Option(..., prompt=True),
                phone: str = typer.Option(..., prompt=True)):
    """Add a new Telegram account."""
    session_name = phone.replace("+", "")
    client = Client(session_name, api_id=api_id, api_hash=api_hash,
                    workdir=SESSIONS_DIR.as_posix())
    client.connect()
    typer.echo("Sending code to Telegram...")
    sent = client.send_code(phone)
    code = typer.prompt("Enter the code you received")
    try:
        client.sign_in(phone_number=phone,
                      phone_code_hash=sent.phone_code_hash,
                      phone_code=code)
    except errors.SessionPasswordNeeded:
        password = typer.prompt("Two-step verification password", hide_input=True)
        client.check_password(password)
    client.disconnect()

    with open(SESSIONS_DIR / f"{session_name}.json", "w") as f:
        json.dump({"api_id": api_id, "api_hash": api_hash, "phone": phone}, f)

    logging.info("Added account %s", phone)
    typer.echo("Account added and session saved.")


async def _is_subscribed(client: Client, channel: str) -> bool:
    try:
        await client.get_chat_member(channel, 'me')
        return True
    except errors.UserNotParticipant:
        return False


@app.command()
def react(channel: str = typer.Argument(...)):
    """Join channel if needed and react to its posts from all accounts."""
    asyncio.run(_react(channel))


async def _react(channel: str):
    configs = list(SESSIONS_DIR.glob("*.json"))
    if not configs:
        typer.echo("No accounts configured.")
        return

    clients = []
    for cfg_path in configs:
        with open(cfg_path) as f:
            cfg = json.load(f)
        client = Client(cfg_path.stem, api_id=cfg["api_id"], api_hash=cfg["api_hash"],
                        workdir=SESSIONS_DIR.as_posix())
        await client.start()
        clients.append(client)
        if not await _is_subscribed(client, channel):
            await client.join_chat(channel)
            logging.info("%s joined %s", cfg_path.stem, channel)

    async for message in clients[0].get_chat_history(channel, limit=100):
        for client in clients:
            try:
                await client.send_reaction(channel, message.id, random.choice(EMOJIS))
                logging.info("%s reacted to %s", client.name, message.id)
            except errors.ReactionInvalid:
                logging.warning("Invalid reaction for %s", client.name)
            except Exception as e:
                logging.error("%s failed on %s: %s", client.name, message.id, e)

    for client in clients:
        await client.stop()


if __name__ == "__main__":
    app()
