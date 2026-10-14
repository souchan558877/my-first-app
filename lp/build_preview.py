"""Embed only the LP's own assets. The official homepage is never modified."""
from pathlib import Path
import base64
import re

ROOT = Path(__file__).resolve().parent


def build():
    index = ROOT / "index.html"
    html = index.read_text(encoding="utf-8")
    svg = base64.b64encode((ROOT / "assets/door.svg").read_bytes()).decode("ascii")
    sections = {
        "LP STYLES": "<style>\n" + (ROOT / "styles.css").read_text(encoding="utf-8") + "\n</style>",
        "LP SCRIPT": "<script>\n" + (ROOT / "script.js").read_text(encoding="utf-8") + "\n</script>",
        "LP IMAGE": f'<img src="data:image/svg+xml;base64,{svg}" alt="淡いピンクのとびらの向こうに広がる、やさしい水色の空" width="620" height="690">',
    }
    for name, content in sections.items():
        start, end = f"<!-- BEGIN {name} -->", f"<!-- END {name} -->"
        pattern = re.escape(start) + r".*?" + re.escape(end)
        html, count = re.subn(pattern, lambda _: f"{start}\n{content}\n{end}", html, flags=re.S)
        if count != 1:
            raise ValueError(f"Expected one {name} section, found {count}")
    index.write_text(html, encoding="utf-8")
    print("lp/index.html refreshed. Official homepage unchanged.")


if __name__ == "__main__":
    build()
