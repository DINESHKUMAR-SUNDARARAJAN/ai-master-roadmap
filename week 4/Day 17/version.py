# version_check.py
import webbrowser
from datetime import datetime

def check_versions():
    # Gemini 2.5 confirmed GA June 17, 2025 :contentReference[oaicite:1]{index=1}
    # GPT‑4.1 & GPT‑4.5 released Feb/Apr 2025 :contentReference[oaicite:2]{index=2}
    latest = {
        "gemini": "2.5",
        "gpt": "4.1"
    }
    # App logic: warn if stored version mismatches
    print(f"{datetime.now()}: Target versions → Gemini {latest['gemini']}, GPT {latest['gpt']}")
    return latest
