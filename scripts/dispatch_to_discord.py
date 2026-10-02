#!/usr/bin/env python3
"""
ALL-SIGNAL // THE CLUB 1 — DISCORD DISPATCH UTILITY
Broadcasts markdown notes, executive briefings, or custom intelligence
directly from the Obsidian vault into the Discord command channel.
"""

import os
import sys
import json
import argparse
import urllib.request
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent

def load_webhook_url():
    env_file = VAULT_ROOT / ".env"
    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("DISCORD_WEBHOOK_URL="):
                    return line.split("=", 1)[1].strip()
    return os.getenv("DISCORD_WEBHOOK_URL")

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", content

def dispatch_note(note_rel_path):
    webhook_url = load_webhook_url()
    if not webhook_url:
        print("[!] Error: DISCORD_WEBHOOK_URL not found in .env or environment.")
        sys.exit(1)

    note_path = VAULT_ROOT / note_rel_path
    if not note_path.exists():
        print(f"[!] Error: Note not found: {note_path}")
        sys.exit(1)

    raw_text = note_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(raw_text)

    # Extract title from first H1 or filename
    lines = body.splitlines()
    title = note_path.stem
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # Truncate preview for embed description (max 2000 chars)
    preview = "\n".join([l for l in lines if not l.startswith("# ")])[:1800]

    payload = {
        "username": "THE CLUB 1 // DISPATCH",
        "avatar_url": "https://raw.githubusercontent.com/All-Signal/.github/main/assets/banner.jpg",
        "embeds": [
            {
                "title": f"📑 VAULT DISPATCH // {title}",
                "description": preview if preview.strip() else "*Empty note content*",
                "color": 8139245,
                "fields": [
                    {
                        "name": "📂 Location",
                        "value": f"`{note_rel_path}`",
                        "inline": True
                    },
                    {
                        "name": "🔗 GitHub Source",
                        "value": f"[View on GitHub](https://github.com/All-Signal/the-club-1/blob/main/{urllib.parse.quote(note_rel_path)})",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "ALL-SIGNAL // The Club 1 Knowledge Vault",
                    "icon_url": "https://github.com/All-Signal.png"
                }
            }
        ]
    }

    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "Club1-Dispatch/1.0"}
    )

    with urllib.request.urlopen(req) as resp:
        if resp.status in (200, 204):
            print(f"[✓] Successfully dispatched '{title}' to Discord.")
        else:
            print(f"[!] Warning: Received status {resp.status}")

def dispatch_message(text):
    webhook_url = load_webhook_url()
    if not webhook_url:
        print("[!] Error: DISCORD_WEBHOOK_URL not found.")
        sys.exit(1)

    payload = {
        "username": "THE CLUB 1 // ORACLE",
        "avatar_url": "https://raw.githubusercontent.com/All-Signal/.github/main/assets/banner.jpg",
        "embeds": [
            {
                "title": "⚡ VAULT SIGNAL",
                "description": text,
                "color": 49087,
                "footer": {
                    "text": "ALL-SIGNAL // The Club 1 Knowledge Vault",
                    "icon_url": "https://github.com/All-Signal.png"
                }
            }
        ]
    }

    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "Club1-Dispatch/1.0"}
    )
    with urllib.request.urlopen(req) as resp:
        print("[✓] Custom signal broadcasted successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dispatch notes to Discord")
    parser.add_argument("--note", help="Relative path to note from vault root")
    parser.add_argument("--msg", help="Broadcast raw text message")
    args = parser.parse_args()

    if args.note:
        dispatch_note(args.note)
    elif args.msg:
        dispatch_message(args.msg)
    else:
        parser.print_help()
