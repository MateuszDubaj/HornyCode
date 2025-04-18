from .transpiler import transpile
from .furify import enable_furry_output

def horny_exec(code: str, globals=None, locals=None):
    enable_furry_output()
    py_code = transpile(code)
    exec(py_code, globals, locals)

def horny_exec_file(path: str):
    with open(path, 'r') as file:
        horny_exec(file.read())

