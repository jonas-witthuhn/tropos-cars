# generate_version_hook.py
import os
import shutil
from pathlib import Path

def generate_version_file():
    # Define paths relative to the project root (where pyproject.toml is)
    # Note: In scikit-build-core hooks, the current working directory is usually the project root
    version_source = Path("external/ecrad_source/VERSION")
    version_dest_dir = Path("src/tcars")
    version_dest_file = version_dest_dir / "_ecrad_version.py"

    if not version_source.exists():
        raise FileNotFoundError(f"Version file not found at {version_source}")

    # Read the version string (strip whitespace/newlines)
    with open(version_source, "r", encoding="utf-8") as f:
        version = f.read().strip()

    # Ensure the destination directory exists
    version_dest_dir.mkdir(parents=True, exist_ok=True)

    # Write the Python version file
    # This creates a module that can be imported as: from package import _ecrad_version
    content = f'''
"""
Auto-generated version file.
Do not edit manually.
"""
__version__ = "{version}"
'''
    
    with open(version_dest_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[scikit-build] Generated version file: {version_dest_file} with version {version}")

if __name__ == "__main__":
    generate_version_file()