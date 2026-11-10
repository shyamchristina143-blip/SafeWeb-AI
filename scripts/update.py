import urllib.request
from pathlib import Path

SOURCE = (
    "https://cdn.jsdelivr.net/gh/"
    "hagezi/dns-blocklists@latest/adblock/nsfw.txt"
)

OUTPUT = Path("blocklists/nsfw.txt")

def update_blocklist():
    print("SafeWeb AI: Updating adult-domain database...")

    request = urllib.request.Request(
        SOURCE,
        headers={"User-Agent": "SafeWeb-AI/0.1"}
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        content = response.read().decode("utf-8")

    lines = content.splitlines()

    domains = [
        line for line in lines
        if line.strip().startswith("||")
        and line.strip().endswith("^")
    ]

    if len(domains) < 1000:
        raise ValueError("Downloaded blocklist failed validation")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")

    print(f"Successfully processed {len(domains)} entries.")

if __name__ == "__main__":
    update_blocklist()
