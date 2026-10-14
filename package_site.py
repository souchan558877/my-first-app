"""Build a downloadable ZIP containing only the site's known public files."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from build_preview import build

ROOT = Path(__file__).resolve().parent
FILES = [
    "index.html", "styles.css", "script.js", "assets/door.svg",
    "README.md", "START-HERE.txt", "build_preview.py", "package_site.py", ".nojekyll",
    "docs/preview-desktop.png", "docs/preview-mobile.png",
]


def package():
    build()
    output = ROOT / "downloads/mezame-no-tobira.zip"
    output.parent.mkdir(exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for filename in FILES:
            content = (ROOT / filename).read_bytes()
            info = ZipInfo("mezame-no-tobira/" + filename, (2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    with ZipFile(output) as archive:
        assert archive.testzip() is None, "ZIP integrity check failed"
    print(f"Created {output.name}: {len(FILES)} files, {output.stat().st_size} bytes")


if __name__ == "__main__":
    package()
