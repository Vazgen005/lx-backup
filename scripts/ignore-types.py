import argparse
from pathlib import Path

# Create an argument parser and add argument for file path
parser = argparse.ArgumentParser(description='Prepend "# type: ignore" to a file.')
parser.add_argument("file", help="The file to prepend to.")
args = parser.parse_args()

# Verify that the file exists
path = Path(args.file)

if not path.is_file():
    raise FileNotFoundError(f"The file {path} does not exist.")

# Prepend the specified string to the file content
with path.open("r+") as f:
    content = f.read()
    if not content.startswith("# type: ignore"):
        f.seek(0, 0)
        f.write("# type: ignore\n" + content)
