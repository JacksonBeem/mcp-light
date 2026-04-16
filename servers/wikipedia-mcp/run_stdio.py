from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

    if "--transport" not in sys.argv:
        sys.argv.extend(["--transport", "stdio"])

    from wikipedia_mcp.__main__ import main as wikipedia_main

    wikipedia_main()


if __name__ == "__main__":
    main()
