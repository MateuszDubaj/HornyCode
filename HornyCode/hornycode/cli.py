import sys
from .hook import horny_exec_file

def main():
    if len(sys.argv) != 2:
        print("Usage: hornyrun <script.hpy>")
        return
    horny_exec_file(sys.argv[1])
