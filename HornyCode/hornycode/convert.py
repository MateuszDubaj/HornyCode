import sys
from .keywords import PYTHON_TO_HORNY
import re

def hornycompile(source: str) -> str:
    for py, horny in PYTHON_TO_HORNY.items():
        pattern = r'\\b' + re.escape(py) + r'\\b'
        source = re.sub(pattern, horny, source)
    return source

def main():
    if len(sys.argv) != 3:
        print("Usage: hornycompile <source.py> <output.hpy>")
        return
    source_file, output_file = sys.argv[1], sys.argv[2]
    with open(source_file, 'r') as f:
        py_code = f.read()
    horny_code = dehornify(py_code)
    with open(output_file, 'w') as f:
        f.write(horny_code)
    print(f"Converted {source_file} -> {output_file}")

