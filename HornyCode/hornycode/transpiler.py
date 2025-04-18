import re
from .keywords import HORNY_TO_PYTHON

def transpile(source: str) -> str:
    for horny, real in HORNY_TO_PYTHON.items():
        pattern = r'\b' + re.escape(horny) + r'\b'
        source = re.sub(pattern, real, source)
    return source

