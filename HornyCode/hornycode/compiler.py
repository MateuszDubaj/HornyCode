import sys
from .transpiler import transpile

def main():
    if len(sys.argv) != 3:
        print("Usage: hornycompile <source.hpy> <output.py>")
        return
    source_file, output_file = sys.argv[1], sys.argv[2]
    with open(source_file, 'r') as f:
        source_code = f.read()
    output_code = transpile(source_code)
    with open(output_file, 'w') as f:
        f.write(output_code)
    print(f"Compiled {source_file} -> {output_file}")

