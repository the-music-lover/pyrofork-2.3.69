import json
import os
from info import URL as DEFAULT_URL, BIN_CHANNEL as DEFAULT_BIN

CONFIG_FILE = "config.json"

def init_config():
    if not os.path.exists(CONFIG_FILE):
        data = {
            "URL": DEFAULT_URL,
            "BIN_CHANNEL": DEFAULT_BIN
        }
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

def read_config():
    init_config()
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def update_config(url: str, bin_channel: str):
    data = {
        "URL": url,
        "BIN_CHANNEL": bin_channel
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
