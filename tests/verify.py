"""Check this snapshot through an installed RXPGuides loader, without an account."""
from pathlib import Path
import hashlib
import re
import subprocess
import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: python3 tests/verify.py "/path/to/RXPGuides" lua5.1')

root = Path(__file__).resolve().parents[1]
rxp = Path(sys.argv[1])
lua = sys.argv[2]
package = root / "RXPDecryptedGuides"
toc = (package / "RXPDecryptedGuides.toc").read_text(encoding="utf-8")
assert "## Dependencies: RXPGuides" in toc
interface = re.search(r"^## Interface:\s*(.*)$", toc, re.M)[1]
assert "16001" in [value.strip() for value in interface.split(",")]
files = [package / line.split(" [")[0] for line in toc.splitlines()
         if line.strip() and not line.startswith("#")]
assert files and all(path.is_file() for path in files), "Missing guide file"
assert (rxp / "GuideLoader.lua").is_file(), "Missing RXPGuides loader"

locales = "enUS deDE esES esMX frFR itIT koKR ptBR ruRU zhCN zhTW".split()
expected = "816fe4f898665b2a65040edac6357a3e5a8713c2465ccc0de5b4dc72e393ce5d"
for locale in locales:
    result = subprocess.run(
        [lua, str(root / "tests/registration.lua"), str(rxp), locale, *map(str, files)],
        check=True, capture_output=True,
    )
    assert not result.stderr, result.stderr.decode()
    assert result.stdout.count(b"\0") == 198, f"Wrong guide count on {locale}"
    assert hashlib.sha256(result.stdout).hexdigest() == expected, f"Changed guide text on {locale}"

print(f"PASS: 198 guides register on {len(locales)} locales without an account API")
print("PASS: registered text matches the validated snapshot")
